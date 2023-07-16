def parse_valves(content: str):
    split_lines = [line.split("; ") for line in content.splitlines()]
    name_ids = {}
    flows: list[int] = []
    entry = 0

    counter = 0
    for first, _ in split_lines:
        name, flow = first.replace("Valve ", "").replace("has flow rate=", "").split()
        if name == "AA":
            entry = counter
        name_ids[name] = counter
        flows.append(int(flow))
        counter += 1

    matrix = [[1000 for _ in range(len(flows))] for _ in range(len(flows))]
    for i in range(len(flows)):
        matrix[i][i] = 0

    counter = 0
    for _, second in split_lines:
        str_targets = (
            second.removeprefix("tunnels lead to valves ")
            .removeprefix("tunnel leads to valve ")
            .split(", ")
        )
        int_targets: list[int] = [name_ids[name] for name in str_targets]
        for target in int_targets:
            matrix[counter][target] = 1
        counter += 1

    return matrix, flows, entry


def floyd_warshall(matrix: list[list[int]]):
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]


def compress(matrix: list[list[int]], flows: list[int], entry: int):
    valve = 0
    while valve < len(flows):
        if flows[valve] == 0 and valve != entry:
            if valve < entry:
                entry -= 1
            flows.pop(valve)
            matrix.pop(valve)
            for row in matrix:
                row.pop(valve)
        else:
            valve += 1
    return entry


def find_solution(
    all_targets: int,
    matrix: list[list[int]],
    flows: list[int],
    open_valves: int,
    current_valve: int,
    time_left: int,
    cache: dict[tuple[int, int, int], int] = {},
    current_best: list[int] = [0],
    pressure: int = 0,
) -> int:
    if (open_valves, current_valve, time_left) in cache:
        return cache[(open_valves, current_valve, time_left)]

    released_pressure = flows[current_valve] * time_left

    theoretical_max = pressure + released_pressure
    remaining_targets = all_targets

    while remaining_targets > 0:
        # isolate rightmost bit of targets
        target = remaining_targets & -remaining_targets
        # remove rightmost bit of targets
        remaining_targets ^= target
        # get counter out of target
        counter = target.bit_length() - 1

        if time_left > matrix[current_valve][counter]:
            theoretical_max += flows[counter] * (
                time_left - matrix[current_valve][counter] - 1
            )

    if theoretical_max < current_best[0]:
        return released_pressure

    best = 0
    remaining_targets = all_targets

    while remaining_targets > 0:
        # isolate rightmost bit of targets
        target = remaining_targets & -remaining_targets
        # remove rightmost bit of targets
        remaining_targets ^= target
        # get counter out of target
        counter = target.bit_length() - 1

        if time_left > matrix[current_valve][counter]:
            best = max(
                best,
                find_solution(
                    all_targets & ~target,
                    matrix,
                    flows,
                    open_valves | target,
                    counter,
                    time_left - matrix[current_valve][counter] - 1,
                    cache,
                    current_best,
                    pressure + released_pressure,
                ),
            )

    best += released_pressure
    current_best[0] = max(best, current_best[0])
    cache[(open_valves, current_valve, time_left)] = best
    return best


def main(input: str):
    matrix, flows, entry = parse_valves(input)
    floyd_warshall(matrix)
    entry = compress(matrix, flows, entry)
    return find_solution(
        ((1 << len(matrix)) - 1) & ~(1 << entry),
        matrix,
        flows,
        1 << entry,
        entry,
        30,
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    print(main(content))

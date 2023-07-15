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
    all_valves: int,
    matrix: list[list[int]],
    flows: list[int],
    open_valves: int,
    current_valve: int,
    time_left: int,
    cache: dict[tuple[int, int, int], int],
) -> int:
    if (open_valves, current_valve, time_left) in cache:
        return cache[(open_valves, current_valve, time_left)]

    targets = all_valves & ~open_valves
    counter = 0
    best = 0

    while (targets >> counter) != 0:
        target = targets & (1 << counter)
        if target != 0 and time_left > matrix[current_valve][counter]:
            tmp = find_solution(
                all_valves,
                matrix,
                flows,
                open_valves | target,
                counter,
                time_left - 1 - matrix[current_valve][counter],
                cache,
            )
            if best < tmp:
                best = tmp

        counter += 1

    best += flows[current_valve] * time_left
    cache[(open_valves, current_valve, time_left)] = best
    return best


def main(input: str):
    matrix, flows, entry = parse_valves(input)
    floyd_warshall(matrix)
    entry = compress(matrix, flows, entry)
    cache = {}

    all_valves = (1 << len(matrix)) - 1
    human_valves = (1 << (len(matrix) // 2)) - 1
    best = 0
    while human_valves < (1 << len(matrix)):
        best = max(
            best,
            find_solution(all_valves, matrix, flows, human_valves, entry, 26, cache)
            + find_solution(
                all_valves, matrix, flows, human_valves ^ all_valves, entry, 26, cache
            ),
        )

        # determine next mask with Gosper's hack
        a = human_valves & -human_valves  # determine rightmost 1 bit
        b = human_valves + a  # determine carry bit
        human_valves = (
            int(((human_valves ^ b) >> 2) / a) | b
        )  # produce block of ones that begins at the least-significant bit

    return best


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    print(main(content))

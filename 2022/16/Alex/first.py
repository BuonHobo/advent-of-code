# name: (name, flow, [t1,t2,t3,...])
def parse_valves(input: str):
    result = {}
    assoc = {}
    counter = 1

    for line in input.splitlines():
        name = line.split("; ")[0].split()[1]
        assoc[name] = counter
        counter = counter << 1

    for line in input.splitlines():
        # Valve II has flow rate=0; tunnels lead to valves AA, JJ
        # Valve JJ has flow rate=21; tunnel leads to valve II
        line = line.split("; ")
        first = line[0].split()
        name = first[1]
        flow = int(first[4].split("=")[1])
        targets = (
            line[1]
            .removeprefix("tunnels lead to valves ")
            .removeprefix("tunnel leads to valve ")
            .split(", ")
        )

        new_targets = 0
        for target in targets:
            new_targets = new_targets | assoc[target]

        result[assoc[name]] = (flow, new_targets)
    return result, assoc["AA"]


def dfs(
    current: int,  # id of the current valve
    time: int,  # remaining minutes
    open: int,  # number representing the open valves
    cache: dict[
        tuple[int, int, int], int
    ],  # (current valve, time, open valves) -> best result
    prev:int,
    valves: dict[int, tuple[int, int]],  # valve id -> (flow, target valves)
):
    if time == 1:
        return 0

    if (res := cache.get((current, time, open))) is not None:
        return res

    flow, targets = valves[current]

    result = 0
    cursor = 1
    targets &= ~prev
    while targets > 0:
        target = targets & cursor
        targets = targets & ~cursor
        cursor <<= 1
        if target != 0:
            result = max(result, dfs(target, time - 1, open, cache, current, valves))

    if flow > 0 and (current & open == 0):
        result = max(
            result,
            flow * (time-1) + dfs(current, time - 1, open | current, cache, 0, valves),
        )

    cache[(current, time, open)] = result
    return result


def main(input: str):
    valves, start = parse_valves(input)
    return dfs(start, 30, 0, {}, 0, valves)


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
    print(main(input))

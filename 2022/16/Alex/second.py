import re


def parse_valves(content: str):
    structured_data: dict[str, tuple[int, list[str]]] = {
        line[0]: (int(line[1]), line[2:])
        for line in (
            re.findall(r"[A-Z]+|\d+", line[1:]) for line in content.splitlines()
        )
    }
    return structured_data


def main(input: str):
    # get structured data: {NAME: flow,neighbours}
    data = parse_valves(input)

    # connect different valves
    distances: dict[tuple[str, str], int] = {
        (src, dst): 1 for src in data for dst in data if dst in data[src][1]
    }

    # store flows in a dict
    flows: dict[str, int] = {
        valve: flow for valve, (flow, _) in data.items() if flow != 0
    }

    bits: dict[str, int] = {valve: 1 << index for index, valve in enumerate(flows)}

    # floyd warshall to calculate distances
    for k in data:
        for i in data:
            for j in data:
                distances[i, j] = min(
                    distances.get((i, j), 1000),
                    distances.get((i, k), 1000) + distances.get((k, j), 1000),
                )

    def visit(
        valve: str,
        minutes: int,
        bitmask: int,
        pressure: int,
        answer: dict[int, int] = {},
    ):
        answer[bitmask] = max(answer.get(bitmask, 0), pressure)
        for valve2, flow in flows.items():
            remaining_minutes = minutes - distances[valve, valve2] - 1
            if remaining_minutes <= 0 or bits[valve2] & bitmask:
                continue
            visit(
                valve2,
                remaining_minutes,
                bitmask | bits[valve2],
                pressure + flow * remaining_minutes,
                answer,
            )
        return answer

    visited2 = visit("AA", 26, 0, 0, {})
    part2 = max(
        v1 + v2
        for bitm1, v1 in visited2.items()
        for bitm2, v2 in visited2.items()
        if not bitm1 & bitm2
    )

    return part2


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    print(main(content))

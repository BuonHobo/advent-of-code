import itertools


def parse_initial(initial: str) -> list[list[str]]:
    stacks = initial.splitlines()
    number = int(max(stacks.pop().split()))

    stacks.reverse()

    verticals = [[] for _ in range(number)]
    for line in stacks:
        for i in range(number):
            verticals[i].append(line[4 * i + 1])

    return list(map(lambda y: list(filter(lambda x: x != " ", y)), verticals))


def parse_moves(moves: str) -> list[tuple[int]]:
    result = []
    for move in moves.splitlines():
        move = move.split()
        move = move[1::2]
        result.append(tuple(map(int, move)))
    return result


def main(input: str) -> str:
    initial, moves = input.split("\n\n")
    initial = parse_initial(initial)
    moves = parse_moves(moves)

    for mov, frm, to in moves:
        initial[to - 1].extend(initial[frm - 1][-mov:])
        initial[frm - 1]=initial[frm - 1][0:-mov]

    res = ""
    for l in initial:
        res += l[-1]
    return res


if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.read()

    print(main(string))

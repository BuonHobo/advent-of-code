import itertools


def compare(primo: int | list, secondo: int | list) -> int:
    """
    Restituisce un valore negativo se primo<secondo,
    positivo se primo>secondo e 0 se primo==secondo
    """
    match (primo, secondo):
        case (int(a), int(b)):  # 4,4
            return a - b
        case (int(a), list(b)):  # 3,[5]
            return compare([a], b)  # ->[3],[5]
        case (list(a), int(b)):  # 3,[5]
            return compare(a, [b])  # ->[3],[5]
        case (list(a), list(b)):
            try:
                for x, y in zip(a, b, strict=True):
                    if (diff := compare(x, y)) == 0:
                        continue
                    else:
                        return diff
                return 0
            except ValueError:
                return len(a) - len(b)
        case _:
            raise ValueError


def main(input: str) -> int:
    i = 1
    j = 2
    for pair in input.split("\n\n"):
        for packet in pair.split("\n"):
            packet = eval(packet)
            if compare(packet, [[6]]) <= 0:
                j += 1
                if compare(packet, [[2]]) <= 0:
                    i += 1

    return i * j


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
    print(main(input))

import itertools


def parse_cave(input):
    cave = set()
    max = 0

    for line in input.splitlines():
        prec_ver = None
        prec_hor = None
        for pair in line.split(" -> "):
            ver, hor = map(int, pair.split(","))
            if prec_ver is not None:
                if ver > prec_ver:
                    punti = ((y, hor) for y in range(prec_ver, ver + 1))
                elif ver < prec_ver:
                    punti = ((y, hor) for y in range(ver, prec_ver + 1))
                elif hor > prec_hor:
                    punti = ((ver, x) for x in range(prec_hor, hor + 1))
                else:
                    punti = ((ver, x) for x in range(hor, prec_hor + 1))
                prec_hor = hor
                prec_ver = ver
            else:
                prec_hor = hor
                prec_ver = ver
                continue

            for v, h in punti:
                if h > max:
                    max = h
                cave.add((v, h))
    return cave, max


def stampa(cave):
    for i in range(11):
        for j in range(494, 504):
            if (j, i) in cave:
                print("o", end="")
            else:
                print(".", end="")
        print()


def main(input):
    cave, max = parse_cave(input)
    max = max + 2

    def is_free(x, y):
        return (x, y) not in cave

    count = 0

    sand: list[tuple[int, int]] = [(500, 0)]
    while True:
        while True:
            x,y=sand[-1]
            if y == max - 1:
                return count

            if is_free(x, y + 1):  # down
                sand.append((x, y + 1))

            elif is_free(x - 1, y + 1):  # left
                sand.append((x - 1, y + 1))

            elif is_free(x + 1, y + 1):  # right
                sand.append((x + 1, y + 1))

            else:  # stopping here
                cave.add((x,y))
                sand.pop()
                break
        count += 1


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
    print(main(input))

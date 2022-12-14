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


def main(input):
    cave, max = parse_cave(input)
    max = max + 2

    def is_free(x, y):
        return (y < max) and (x, y) not in cave

    count = 0
    while is_free(500,0):
        count += 1
        sandx, sandy = 500, 0
        while True:
            if is_free(sandx, sandy + 1):  # down
                sandy += 1

            elif is_free(sandx - 1, sandy + 1):  # left
                sandx -= 1

            elif is_free(sandx + 1, sandy + 1):  # right
                sandx += 1

            else:  # stopping here
                cave.add((sandx, sandy))
                break
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
    print(main(input))

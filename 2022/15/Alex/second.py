import itertools


def man_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


class sen:
    def __init__(self, pos: tuple[int, int], beacon: tuple[int, int]) -> None:
        self.pos = pos
        self.dist = man_dist(beacon, self.pos)

    def in_exc_rng(self, point):
        return self.dist >= man_dist(self.pos, point)

    def __repr__(self) -> str:
        return f"{self.pos},{self.dist}"


def parse(string: str) -> list[sen]:
    res: list[sen] = []
    for line in string.splitlines():
        first, second = line.split(": ")
        x, y = first[12:].split(", ")
        x = int(x)
        y = int(y[2:])

        bx, by = second[23:].split(", ")
        bx = int(bx)
        by = int(by[2:])
        res.append(sen((x, y), (bx, by)))

    return res


def is_free(pos, sensors: list[sen]) -> bool:
    for sensor in sensors:
        if sensor.in_exc_rng(pos):
            return False
    return True


def main(input):
    mx = 4000000
    sensors = parse(input)
    rette: dict[tuple[bool, int], int] = {}

    for sensor in sensors:
        r1 = (True, sensor.pos[1] - sensor.dist - 1 - sensor.pos[0])  # top rising
        r2 = (False, sensor.pos[1] - sensor.dist - 1 + sensor.pos[0])  # top descending
        r3 = (True, sensor.pos[1] + sensor.dist + 1 - sensor.pos[0])  # bot rising
        r4 = (False, sensor.pos[1] + sensor.dist + 1 + sensor.pos[0])  # bot descending

        for r in [r1, r2, r3, r4]:
            if r in rette:
                rette[r] += 1
            else:
                rette[r] = 1

    up = []
    down = []

    for r, c in rette.items():
        if c > 1:
            if r[0]:
                down.append(r)
            else:
                up.append(r)
    points = []

    for ru in up:
        for rd in down:
            point = (ru[1] - rd[1]) // 2
            point = (point, point + rd[1])
            points.append(point)

    for point in points:
        if point[1] not in range(0, mx) or point[0] not in range(0, mx):
            continue
        if is_free(point, sensors):
            return point[0] * 4000000 + point[1]


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
    print(main(input))

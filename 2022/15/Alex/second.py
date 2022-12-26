import itertools


class sen:
    def __init__(self, pos: tuple[int, int], beacon: tuple[int, int]) -> None:
        self.pos = pos
        self.beacon = beacon
        self.dist = abs(self.beacon[0] - self.pos[0]) + abs(
            self.beacon[1] - self.pos[1]
        )
    def __repr__(self) -> str:
        return f"{self.pos},{self.dist}"


def overlaps(range1: tuple[int, int], range2: tuple[int, int]) -> bool:
    return (
        range2[0] <= range1[0] <= range2[1]
        or range2[0] <= range1[0] <= range2[1]
        or range1[0] <= range2[0] <= range1[1]
        or range1[0] <= range2[0] <= range1[1]
    )


class exc_range:
    def __init__(self) -> None:
        self.rngs = []

    def add(self, start, stop) -> None:
        res: list[tuple[int, int]] = []
        additional: list[tuple[int, int]] = []
        for rngs, rnge in self.rngs:
            if overlaps((rngs, rnge), (start, stop)):
                additional.append((min(start, rngs), max(stop, rnge)))
            else:
                res.append((rngs, rnge))

        if len(additional) >= 1:
            mins = min(map(lambda tup: tup[0], additional))
            maxe = max(map(lambda tup: tup[1], additional))
            res.append((mins, maxe))
        else:
            res.append((start, stop))

        self.rngs = res

    def rem(self, point) -> None:
        res: list[tuple[int, int]] = []
        for rngs, rnge in self.rngs:
            if rngs < point < rnge:
                res.append((rngs, point - 1))
                res.append((point + 1, rnge))
            elif point == rngs:
                res.append((point + 1, rnge))
            elif point == rnge:
                res.append((rngs, point - 1))
            else:
                res.append((rngs, rnge))
        self.rngs = res


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


def unavailable_positions(y: int, sensors: list[sen],mx=4000000) -> list[tuple[int, int]]:
    res: exc_range = exc_range()

    for sensor in sensors:
        distance = sensor.dist - abs(y - sensor.pos[1])
        if distance <= 0:
            continue
        start = sensor.pos[0] - distance
        start = max(start, 0)
        stop = sensor.pos[0] + distance
        stop = min(stop, mx)
        res.add(start, stop)

    return res.rngs


def main(input):
    mx=4000000
    sensors = parse(input)
    #sensors:list[sen]=[sen((4,3),(4,1))]
    rette: dict[tuple[bool, int], int] = {}

    for sensor in sensors:
        r1 = (True,  sensor.pos[1] - sensor.dist - 1 - sensor.pos[0])  # top rising
        r2 = (False, sensor.pos[1] - sensor.dist - 1 + sensor.pos[0])  # top descending
        r3 = (True,  sensor.pos[1] + sensor.dist + 1 - sensor.pos[0])  # bot rising
        r4 = (False, sensor.pos[1] + sensor.dist + 1 + sensor.pos[0])  # bot descending

        for r in [r1,r2,r3,r4]:
            if r in rette:
                rette[r]+=1
            else:
                rette[r]=1

    up=[]
    down=[]

    for r,c in rette.items():
        if c>1:
            if r[0]:
                down.append(r)
            else:
                up.append(r)
    punti=[]

    for ru in up:
        for rd in down:
            punto=(ru[1]-rd[1])//2
            punto=(punto,punto+rd[1])
            punti.append(punto)

    for punto in punti:
        if punto[1] not in range(0,mx):
            continue
        if len(pos:=unavailable_positions(punto[1],sensors,mx))>1 and pos[0][1]+1!=pos[1][0]:
            return (pos[-1][0]-1)*4000000+punto[1]

    print(down,up)


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
    print(main(input))

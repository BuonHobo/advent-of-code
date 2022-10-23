def fun(string):
    return (int(x) for x in string.split(","))  # "945,283" -> (945, 283)


def parse_interval(line: str):
    # "821,643 through 882,674" -> ["821,643", "882,674"]
    first, second = line.split(" through ")

    x1, y1 = fun(first)
    x2, y2 = fun(second)

    x_range = range(x1, x2 + 1)
    y_range = range(y1, y2 + 1)

    return (x_range, y_range)


def turn_on(lights, x, y):
    lights[x][y] += 1


def turn_off(lights, x, y):
    lights[x][y] = max(0,lights[x][y]-1)


def toggle(lights, x, y):
    lights[x][y] += 2


def main(input: str) -> int:
    lights = [[0 for _ in range(1000)] for _ in range(1000)]  # Crea la matrice

    for line in input.splitlines():
        if line.startswith("turn on"):  # Le luci vanno accese
            line = line[8:]  # Il resto del comando parte da 8
            handler = turn_on
        elif line.startswith("turn off"):  # Le luci vanno spente
            line = line[9:]
            handler = turn_off
        else:  # Le luci vanno invertite
            line = line[7:]
            handler = toggle
        x_range, y_range = parse_interval(line)

        for x in x_range:
            for y in y_range:
                handler(lights, x, y)

    count = 0
    for row in lights:
        for col in row:
            count += col

    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.read()

    print(main(string))

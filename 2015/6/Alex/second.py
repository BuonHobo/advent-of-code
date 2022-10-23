def parse_interval(line: str):
    first, second = line.split(" through ")

    def fun(string):
        return (int(x) for x in string.split(","))  # 945,283 -> (int(945),int(283))

    x1, y1 = fun(first)
    x2, y2 = fun(second)

    x_range = range(x1, x2 + 1)
    y_range = range(y1, y2 + 1)

    return (x_range, y_range)


def main(input: str) -> int:
    lights = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in input.splitlines():
        if line.startswith("turn on"):

            def handler(x, y):
                lights[x][y] += True

            line = line[8:]
        elif line.startswith("turn off"):

            def handler(x, y):
                lights[x][y] = max(0, lights[x][y] - 1)

            line = line[9:]
        else:

            def handler(x, y):
                lights[x][y] += 2

            line = line[7:]

        x_range, y_range = parse_interval(line)

        for x in x_range:
            for y in y_range:
                handler(x, y)

    count = 0
    for row in lights:
        for col in row:
            count += col

    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.read()

    print(main(string))

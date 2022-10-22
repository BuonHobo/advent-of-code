def main(input: str) -> int:
    x: int = 0
    x2: int = 0
    y: int = 0
    y2: int = 0
    houses: set[tuple[int, int]] = {(0, 0)}
    toggle: bool = True

    for letter in input:
        if toggle:
            match letter:
                case "^":
                    y += 1
                case ">":
                    x += 1
                case "<":
                    x -= 1
                case "v":
                    y -= 1
            houses.add((x, y))
        else:
            match letter:
                case "^":
                    y2 += 1
                case ">":
                    x2 += 1
                case "<":
                    x2 -= 1
                case "v":
                    y2 -= 1
            houses.add((x2, y2))

        toggle = not toggle

    return len(houses)


if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.readline()

    print(main(string))

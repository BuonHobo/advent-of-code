def main(input: str) -> int:
    x: int = 0
    y: int = 0
    houses: set[tuple[int, int]] = {(0, 0)}
    for letter in input:
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
    return len(houses)


if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.readline()

    print(main(string))

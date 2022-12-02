"""
Rock:     0
Paper:    1
Scissors: 2
"""


def get_shape(letter):
    match letter:
        case "A" | "X":
            return 0
        case "B" | "Y":
            return 1
        case "C" | "Z":
            return 2
    return 0


def main(input: str) -> int:
    score = 0
    for match in input.splitlines():
        first, second = match.split(" ")
        first = get_shape(first)

        match second:
            case "X":
                second = (first - 1) % 3
                outcome = 0
            case "Y":
                second = first
                outcome = 3
            case "Z":
                second = (first + 1) % 3
                outcome = 6
            case _:
                second = 0
                outcome = 0

        score += second + 1 + outcome
    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.read()

    print(main(string))

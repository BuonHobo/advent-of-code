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
        first, second = get_shape(first), get_shape(second)
        score += (
            second
            + 1
            + (6 if ((first + 1) % 3 == second) else (3 if first == second else 0))
        )
    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.read()

    print(main(string))

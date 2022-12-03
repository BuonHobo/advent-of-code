def get_priority(letter: str):
    if ord(letter) >= (a := ord("a")):
        return ord(letter) - a + 1

    return ord(letter) - ord("A") + 1 + 26


def split_rucksack(string: str) -> tuple[set[str], set[str]]:
    divider = len(string) // 2
    first = set(list(string[:divider]))
    second = set(list(string[divider:]))
    return first, second


def main(input: str) -> int:
    rucksacks=(split_rucksack(string) for string in input.splitlines())
    priority = 0
    for first,second in rucksacks:
        priority += get_priority(first.intersection(second).pop())
    return priority


if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.read()

    print(main(string))

def get_priority(letter: str):
    if ord(letter) >= (a := ord("a")):
        return ord(letter) - a + 1

    return ord(letter) - ord("A") + 1 + 26


def main(input: str) -> int:
    rucksacks= [set(list(rucksack)) for rucksack in input.splitlines()]
    priority = 0
    for index in range(0,len(rucksacks),3):
        common=rucksacks[index]
        common=common.intersection(rucksacks[index+1])
        common=common.intersection(rucksacks[index+2])
        priority+=get_priority(common.pop())
    return priority


if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.read()

    print(main(string))

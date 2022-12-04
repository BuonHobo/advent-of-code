import itertools


def overlaps(range1: tuple[int, int], range2: tuple[int, int]) -> bool:
    return (
        range2[0] <= range1[0] <= range2[1]
        or range2[0] <= range1[1] <= range2[1]
        or range1[0] <= range2[0] <= range1[1]
        or range1[0] <= range2[1] <= range1[1]
    )


def main(input: str) -> int:

    return sum(
        int(
            overlaps(
                *map(lambda x: tuple(int(num) for num in x.split("-")), pair.split(","))
            )
        )
        for pair in input.splitlines()
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.read()

    print(main(string))

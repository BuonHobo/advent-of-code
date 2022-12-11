import itertools
import typing


class monkey:
    def __init__(
        self,
        id: int,
        items: list[int],
        inspection: typing.Callable[[int], int],
        test: int,
        target: tuple[int, int],
    ) -> None:
        self.id = id
        self.items = items
        self.inspection = inspection
        self.test = test
        self.target = target
        self.count = 0
        self.div = 0

    def inspect_item(self, worry: int) -> int:
        self.count += 1
        return self.inspection(worry) % self.div

    def throw_items(self) -> map:
        """returns (worry,target)"""
        return map(
            lambda worry: (worry, self.target[0])
            if worry % self.test == 0
            else (worry, self.target[1]),
            map(self.inspect_item, self.items)
        )


def parse_monkey(string: str) -> monkey:
    id, items, inspect, test, iftrue, iffalse = string.split("\n")

    id = int(id[7])

    items = list(map(int, items[18:].split(", ")))

    test = test.partition("by ")[2]
    test = int(test)

    num=inspect[25:]
    inspect=inspect[23]

    if inspect == "*":
        sign = int.__mul__
    else:
        sign = int.__add__

    if num.isdecimal():
        op: typing.Callable[[int], int] = lambda old: sign(old, int(num))
    else:
        op: typing.Callable[[int], int] = lambda old: sign(old, old)

    iftrue = iftrue[-1]
    iftrue = int(iftrue)

    iffalse = iffalse[-1]
    iffalse = int(iffalse)

    return monkey(id, items, op, test, (iftrue, iffalse))


def main(input: str) -> int:
    monkeys = tuple(map(parse_monkey, input.split("\n\n")))

    divisibility = 1
    for monke in monkeys:
        divisibility *= monke.test

    for monkey in monkeys:
        monkey.div = divisibility

    rounds = 10000

    for _ in range(rounds):
        for monke in monkeys:
            for worry, target in monke.throw_items():
                monkeys[target].items.append(worry)
            monke.items.clear()

    res = sorted(map(lambda monke: monke.count, monkeys), reverse=True)
    return res[0] * res[1]


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    print(main(input))

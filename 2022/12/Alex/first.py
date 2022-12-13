import itertools


def main(input: str) -> int:
    input: list[list[int]] = [
        [
            ord(char if char not in "ES" else ("a" if char == "S" else "z"))
            for char in line
        ]
        for line in input.splitlines()
    ]

    h, w = len(input), len(input[0])

    def neighbours(i, j):
        res = []

        if i > 0:
            res.append((i - 1, j))
        if i < h - 1:
            res.append((i + 1, j))
        if j > 0:
            res.append((i, j - 1))
        if j < w - 1:
            res.append((i, j + 1))

        return res

    def get_num(i, j):
        return input[i][j]

    start = (20, 0)
    end = (20, 148)

    visited: set[tuple[int, int]] = {start}
    visit_queue: list[tuple[int, int]] = list(
        filter(
            lambda x: get_num(*x) - get_num(*start) <= 1,
            neighbours(*start),
        )
    )

    finish: bool = False
    count = 0

    while not finish:
        count += 1
        new_visit_queue = []
        
        while len(visit_queue) > 0:
            current = visit_queue.pop()
            if current == end:
                finish = True
                break

            new_visit_queue.extend(
                filter(
                    lambda x: x not in visit_queue
                    and x not in new_visit_queue
                    and x not in visited
                    and get_num(*x) - get_num(*current) <= 1,
                    neighbours(*current),
                )
            )
            visited.add(current)

        visit_queue = new_visit_queue

    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
    print(main(input))

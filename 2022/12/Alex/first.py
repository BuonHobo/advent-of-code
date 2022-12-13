import itertools


def main(input: str) -> int:

    data: list[list[int]] = []
    start=end=(0,0)

    for i, line in enumerate(input.splitlines()):
        buffer: list[int] = []
        for j, char in enumerate(line):
            if char == "S":
                start = (i, j)
                buffer.append(ord("a"))
            elif char == "E":
                end = (i, j)
                buffer.append(ord("z"))
            else:
                buffer.append(ord(char))
        data.append(buffer)

    h, w = len(data), len(data[0])

    def neighbours(cell:tuple[int,int]):
        i, j = cell
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

    def get_num(point):
        return data[point[0]][point[1]]

    def is_accessible(src:tuple[int,int],dest:tuple[int,int]):
        return get_num(dest)-get_num(src)<=1

    visited: set[tuple[int, int]] = {start}
    visit_queue: list[tuple[int, int]] = list(
        filter(
            lambda x: is_accessible(start,x),
            neighbours(start),
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
                    and is_accessible(current,x),
                    neighbours(current),
                )
            )
            visited.add(current)

        visit_queue = new_visit_queue

    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
    print(main(input))

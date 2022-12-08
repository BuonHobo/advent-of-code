class tree:
    def __init__(self, height: int) -> None:
        self.height = height
        self.up: tree | None = None
        self.down: tree | None = None
        self.left: tree | None = None
        self.right: tree | None = None

    def is_visible(self) -> bool:
        for attr in ("up", "left", "right", "down"):
            tr = self
            result = True
            while (tr := tr.__getattribute__(attr)) is not None:
                if self.height <= tr.height:
                    result = False
                    break

            if result == True:
                return True

        return False

    def __repr__(self) -> str:
        return str(self.height)


def build_graph(input: str) -> list[list[tree]]:
    numbers: list[list[int]] = [
        [int(char) for char in line] for line in input.splitlines()
    ]

    trees: list[list[tree]] = [[tree(0) for num in col] for col in numbers]

    # assign first row
    for i, tr in enumerate(trees[0]):
        tr.height = numbers[0][i]

    # assign last row
    for i, tr in enumerate(trees[-1]):
        tr.height = numbers[-1][i]

    # assign first col
    for i, tr in enumerate(trees[1:-1]):
        tr[0].height = numbers[i + 1][0]

    # assign last col
    for i, tr in enumerate(trees[1:-1]):
        tr[-1].height = numbers[i + 1][-1]

    for row in range(1, len(numbers) - 1):
        for col in range(1, len(numbers[row]) - 1):
            current_tree = trees[row][col]
            current_tree.height = numbers[row][col]

            # check up
            current_tree.up = trees[row - 1][col]

            # check down
            current_tree.down = trees[row + 1][col]

            # check right
            current_tree.right = trees[row][col + 1]

            # check left
            current_tree.left = trees[row][col - 1]

    return trees


def main(input: str) -> int:
    trees = build_graph(input)
    count = 2 * (len(trees[0]) + len(trees) - 2)

    for line in trees[1:-1]:
        for tr in line[1:-1]:
            count += int(tr.is_visible())

    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.read()

    print(main(string))

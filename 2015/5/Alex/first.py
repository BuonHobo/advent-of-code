def main(input: str) -> int:
    forbidden = ["ab", "cd", "pq", "xy"]
    count = 0
    for string in input.splitlines():
        for part in forbidden:
            if part in string:
                break

        else:
            vowels = 0
            double = 0

            for index, letter in enumerate(string[:-1]):
                
                if letter in "aeiou":
                    vowels += 1
                if letter == string[index + 1]:
                    double += 1

            if string[-1] in "aeiou":
                vowels += 1

            if vowels >= 3 and double >= 1:
                count += 1

    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.read()

    print(main(string))

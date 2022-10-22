def main(input: str) -> int:
    forbidden = ["ab", "cd", "pq", "xy"]
    count = 0
    for string in input.splitlines():
        for part in forbidden:
            if part in string:
                break

        else:
            vowels = 0
            double = False

            for index, letter in enumerate(string[:-1]):
                
                vowels += letter in "aeiou"
                
                double = double or letter == string[index + 1]

            vowels += string[-1] in "aeiou"

            count += vowels >= 3 and double

    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.read()

    print(main(string))

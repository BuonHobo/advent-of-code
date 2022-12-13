def main(input: str) -> int:
    count = 0
    for string in input.splitlines():

        length = len(string)
        repeat = False

        for i in range(2, length):
            repeat = repeat or string[i] == string[i - 2]

        if not repeat:
            continue

        coppie = set()
        doppio = False
        vecchia = None

        for i in range(1, length):
            coppia = string[i - 1] + string[i]

            if coppia == vecchia:
                vecchia = None
                continue
            vecchia = coppia

            doppio = doppio or coppia in coppie
            coppie.add(coppia)

        count += doppio

    return count

if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.readlines()

    print(main(string))

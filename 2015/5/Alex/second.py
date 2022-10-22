def main(input: str) -> int:
    count = 0
    for string in input.splitlines():

        repeat = False
        doppio = False
        doppie = {string[0]+string[1]}

        for index, prima in enumerate(string[:-2]):
            if doppio and repeat:
                break

            seconda = string[index + 1]
            terza = string[index + 2]

            repeat = repeat or prima == terza

            doppia = seconda + terza
            if doppia in doppie:
                if index+3<len(string):
                        doppio =doppio or (prima!=terza and terza!=string[index+3])
                else:
                    doppio=doppio or prima!=terza
            else:
                doppie.add(doppia)

        if repeat and doppio:
            count += 1

    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.read()

    print(main("qjhvhtzxzqqjkmpb"))
    print(main("xxyxx"))
    print(main("uurcxstgmygtbstg"))
    print(main("ieodomkazucvgmuy"))
    print(main(string))

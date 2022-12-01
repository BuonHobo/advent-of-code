def main(input:str)->int:
    return max(
        sum(
            int(number) for number in line.splitlines()
            ) 
            for line in input.split("\n\n")
        )

if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.read()

    print(main(string))

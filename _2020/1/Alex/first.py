def main(input:str)->int:
    interi= list(int(numero) for numero in input.splitlines())

    for i in range(0,len(interi)-1):
        for j in range(i,len(interi)):
            if interi[i]+interi[j]==2020:
                return interi[i]*interi[j]
    else:
        raise ValueError

if __name__ == "__main__":
    with open("input.txt") as f:
        string = f.read()

    print(main(string))

import itertools


def parse_cave(input):
    cave:dict[int,set[int]] = {} # {x1: {y1,y2,y3}}
    max = 0

    for line in input.splitlines():
        prec_ver = 0
        prec_hor = 0
        flag = False
        for pair in line.split(" -> "):
            ver, hor = map(int, pair.split(","))
            if flag:
                if ver > prec_ver:
                    punti = ((y, hor) for y in range(prec_ver, ver + 1))
                elif ver < prec_ver:
                    punti = ((y, hor) for y in range(ver, prec_ver + 1))
                elif hor > prec_hor:
                    punti = ((ver, x) for x in range(prec_hor, hor + 1))
                else:
                    punti = ((ver, x) for x in range(hor, prec_hor + 1))
                prec_hor = hor
                prec_ver = ver
            else:
                prec_hor = hor
                prec_ver = ver
                flag = True
                continue

            for v, h in punti:
                if h > max:
                    max = h
                if h not in cave:
                    cave[h]=set()

                cave[h].add(v)
                    
    return cave, max

def stampa(linea):
    for i in range(485,516):
        if i in linea:
            print("o",end="")
        else:
            print(".",end="")
    print()

def main(input):
    cave, max = parse_cave(input)
    max = max + 2

    step=1
    count=0
    current:set[int]={500}
    
    while step<=max:
        attempt:set[int]=set()
        count+=len(current)
        for x in current:
            attempt.add(x)
            attempt.add(x-1)
            attempt.add(x+1)
        if step in cave:
            attempt.difference_update(cave[step])

        current=attempt
        step+=1
    
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
    print(main(input))

        sandx,sandy=500,0
import itertools


def parse_cave(input:str)->dict[int,list[int]]:
    cave:dict[int,list[int]]={}


    for line in input.splitlines():
        prec_ver=None
        prec_hor=None
        for pair in line.split(" -> "):
            ver,hor=map(int,pair.split(","))
            if prec_ver is not None:
                if ver>prec_ver:
                    punti=((y,hor) for y in range(prec_ver,ver+1))
                elif ver<prec_ver:
                    punti=((y,hor) for y in range(ver,prec_ver))
                elif hor>prec_hor:
                    punti=((ver,x) for x in range(prec_hor,hor+1))
                else:
                    punti=((ver,x) for x in range(hor,prec_hor))
                prec_hor=hor
                prec_ver=ver
            else:
                prec_hor=hor
                prec_ver=ver
                continue

            for v,h in punti:
                if v not in cave:
                    cave[v]=[h]
                else:
                    cave[v].append(h)
    return cave

def main(input: str) -> int:
    cave= parse_cave(input)

    falling=True
    count=-1
    while falling:
        count+=1
        sandx,sandy=500,0
        while True:
            try:
                obstacle=min(filter(lambda x: x>sandy,cave[sandx]))
            except:
                falling=False
                break

            sandy=obstacle-1
            try:
                if (sandy+1) not in cave[sandx-1]:
                    sandx=sandx-1
                    sandy=sandy+1
                
                elif (sandy+1) not in cave[sandx+1]:
                    sandx=sandx+1
                    sandy=sandy+1

                else:
                    cave[sandx].append(sandy)
                    break
                    
            except:
                falling=False
                break
    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
    print(main(input))

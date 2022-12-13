import itertools


def compare(primo: int | list, secondo: int | list) -> int:
    """
    Restituisce un valore negativo se primo<secondo,
    positivo se primo>secondo e 0 se primo==secondo
    """
    match (primo, secondo):
        case (int(a), int(b)):  # 4,4
            return a - b
        case (int(a), list(b)):     # 3,[5]
            return compare([a], b)  # ->[3],[5]
        case (list(a), int(b)):     # 3,[5]
            return compare(a, [b])  # ->[3],[5]
        case (list(a),list(b)):
            try:
                for x,y in zip(a,b,strict=True):
                    if (diff:=compare(x,y))==0:
                        continue
                    else: 
                        return diff
                return 0
            except ValueError:
                return len(a)-len(b)
        case _:
            raise ValueError


def main(input: str) -> int:
    i=1
    result=0
    for packet in input.split("\n\n"):
        left,right=packet.split("\n")
        left=eval(left)
        right=eval(right)
        if (compare(left,right)<=0):
            result+=i
        i+=1

    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
    print(main(input))

def all_different(chars:str)->bool:
    return len(set(chars))==len(chars)

def main(input:str)->int:
    for i in range(len(input)-14):
        if all_different(input[i:i+14]):
            return i+14

if __name__=="__main__":
    with open("input.txt") as f:
        input=f.read()
    
    print(main(input))
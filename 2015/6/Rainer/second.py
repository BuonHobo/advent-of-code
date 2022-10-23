def readFile(textFile):
    return open(textFile,'r').read()

def action(move,x1,y1,x2,y2,matrix):
    for i in range(x1,x2 + 1):
        for j in range(y1,y2 + 1):
            if move == "on":
                matrix[i][j] += 1
            elif move == "off":
                if matrix[i][j] > 0:
                    matrix[i][j] -= 1
            elif move == "toggle":
                matrix[i][j] += 2

def splitCommand(input):
    if input[0] == "turn":
        input.pop(0)
    input.pop(2)
    fst = input[1].split(",")
    fst[0] = int(fst[0])
    fst[1] = int(fst[1])
    snd = input[2].split(",")
    snd[0] = int(snd[0])
    snd[1] = int(snd[1])
    
    return [input[0],fst,snd]

def main(input):
    totalBrightness = 0
    matrix = [[0 for _ in range(1000)] for _ in range(1000)]
    bigList = input.splitlines()
    for lst in bigList:
        command = splitCommand(lst.split())
        action(command[0],command[1][0],command[1][1],command[2][0],command[2][1],matrix)
    for i in range(0,1000):
        for j in range(0,1000):
            totalBrightness += matrix[i][j]
    return totalBrightness
    
        
if __name__ == "__main__":
    main(readFile('input.txt'))
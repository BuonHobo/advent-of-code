def readFile(textFile):
    return open(textFile,'r').read()

def action(move,x1,y1,x2,y2,openLightsCoord):
    for i in range(x1,x2 + 1):
        for j in range(y1,y2 + 1):
            if move == "on":
                openLightsCoord.add((i,j))
            elif move == "off":
                if (i,j) in openLightsCoord:
                    openLightsCoord.remove((i,j))
            elif move == "toggle":
                if (i,j) in openLightsCoord:
                    openLightsCoord.remove((i,j))
                else:
                    openLightsCoord.add((i,j))

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
    coordinates = set()
    bigList = input.splitlines()
    for lst in bigList:
        command = splitCommand(lst.split())
        action(command[0],command[1][0],command[1][1],command[2][0],command[2][1],coordinates)
    return len(coordinates)
        
if __name__ == "__main__":
    main(readFile('input.txt'))
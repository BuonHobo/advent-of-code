def readFile(textFile):
    return open(textFile,'r').read()

def on(i,j,openLightsCoord,brightness):
    openLightsCoord.add((i,j))
    if (i,j) in brightness:
        brightness[(i,j)] += 1
    else:
        brightness[(i,j)] = 1

def off(i,j,openLightsCoord,brightness):
    if (i,j) in openLightsCoord:
        openLightsCoord.remove((i,j))
        if brightness.get((i,j)) > 0:
            brightness[(i,j)] -= 1


def action(move,x1,y1,x2,y2,openLightsCoord,brightness):
    for i in range(x1,x2 + 1):
        for j in range(y1,y2 + 1):
            if move == "on":
                on(i,j,openLightsCoord,brightness)
            elif move == "off":
                off(i,j,openLightsCoord,brightness)
            elif move == "toggle":
                openLightsCoord.add((i,j))
                if (i,j) in brightness:
                    brightness[(i,j)] += 2
                else:
                    brightness[(i,j)] = 2
            

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
    brightness = dict()
    brightLevel = 0

    bigList = input.splitlines()
    for lst in bigList:
        command = splitCommand(lst.split())
        action(command[0],command[1][0],command[1][1],command[2][0],command[2][1],coordinates,brightness)

    for bright in brightness.values():
        brightLevel += bright
    return brightLevel
    
        
if __name__ == "__main__":
    #print(main(readFile('input.txt')))
    print(main("turn on 0,0 through 0,0"))
    print(main("toggle 0,0 through 999,999"))
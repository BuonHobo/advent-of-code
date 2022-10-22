def readFile(textFile):
    return open(textFile,'r').readline()

def countHouse(currentPos,visitedHouse):
    if visitedHouse.count(currentPos) > 0:
        return 0
    else:
        visitedHouse.append(currentPos)
        return 1


def main(input):
    visited = 1
    xPos = 0
    yPos = 0
    visitedPos = [[0,0]]
    for ele in input:
        if ele == '>':
            xPos += 1
        elif ele == '<':
            xPos -= 1
        elif ele == '^':
            yPos += 1
        elif ele == 'v':
            yPos -= 1
        pos = [xPos,yPos]
        visited += countHouse(pos,visitedPos)
    return visited

print(main(readFile('input.txt')))
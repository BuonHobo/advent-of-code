class gifter:
    def __init__(self,x,y,visited):
        self.x = x
        self.y = y
        self.visited = visited

def readFile(textFile):
    return open(textFile,'r').readline()

def countHouse(currentPos,visitedHouse):
    if visitedHouse.count(currentPos) > 0:
        return 0
    else:
        visitedHouse.append(currentPos)
        return 1

def updateGifter(move,list,Gifter):
    for move in input:
        if move == '>':
            Gifter.x += 1
        elif move == '<':
            Gifter.x -= 1
        elif move == '^':
            Gifter.y += 1
        elif move == 'v':
            Gifter.y -= 1
        pos = [Gifter.x,Gifter.y]
        visited += countHouse(pos,visitedPos)

def main(input):
    santa = gifter(0,0,1)
    robot = gifter(0,0,0)
    visitedPos = [[0,0]]
    for move in input:
        if move == '>':
            xPos += 1
        elif move == '<':
            xPos -= 1
        elif move == '^':
            yPos += 1
        elif move == 'v':
            yPos -= 1
        pos = [xPos,yPos]
        visited += countHouse(pos,visitedPos)
    return visited
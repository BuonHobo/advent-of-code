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

def main(input):
    santa = gifter(0,0,1)
    robot = gifter(0,0,0)
    visitedHouse = [[0,0]]
    turn = 1
    for el in input:
        Gifter = gifter(0,0,0)
        if turn > 0:
            Gifter = santa
        else:
            Gifter = robot
        turn *= -1

        if el == '>':
            Gifter.x += 1
        elif el == '<':
            Gifter.x -= 1
        elif el == '^':
            Gifter.y += 1
        elif el == 'v':
            Gifter.y -= 1
        pos = [Gifter.x,Gifter.y]
        Gifter.visited += countHouse(pos,visitedHouse)

    return santa.visited + robot.visited

if __name__ == "__main__":
    print(main(readFile('input.txt')))
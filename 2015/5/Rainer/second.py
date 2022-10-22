def readFile(textFile):
    return open(textFile,'r').read()

def firstCondition(niceString):
    i = 1
    stillNotFound = True
    while i < len(niceString) and stillNotFound:
        if findPair(niceString[i - 1],niceString[i],niceString[(i + 1):]):
            stillNotFound = False
        i += 1
    return not(stillNotFound)

def findPair(fst,snd, niceString):
    if len(niceString) < 2:
        return False
    else:
        i = 1
        stillNotFound = True
        while i < len(niceString) and stillNotFound:
            if niceString[i - 1] == fst and niceString[i] == snd:
                stillNotFound = False
            i += 1
        return not(stillNotFound)
            

def secondCondition(niceString):
    i = 2
    stillNotFound = True
    while i < len(niceString) and stillNotFound:
        if niceString[i - 2] == niceString[i]:
            stillNotFound = False
        i += 1
    return not(stillNotFound)

def main(niceString):
    bigList = niceString.splitlines()
    n = 0
    for lts in bigList:
        n += int(firstCondition(lts) and secondCondition(lts))
    return n

if __name__ == "__main__":
    print(main(readFile('input.txt')))


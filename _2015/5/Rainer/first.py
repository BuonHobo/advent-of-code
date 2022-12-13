def readFile(textFile):
    return open(textFile,'r').read()

def firstCondition(niceString):
    if niceString == "" or len(niceString) < 3:
        return False
    else:
        vowels = 0
        for c in niceString:
            vowels += int(c in {'a','e','i','o','u'})
        return vowels > 2

def secondCondition(niceString):
    if niceString == "" or len(niceString) < 2:
        return False
    else:
        i = 1
        stillNotFound = True
        while i < len(niceString) and stillNotFound:
            if niceString[i - 1] == niceString[i]:
                stillNotFound = False
            i += 1
        return not(stillNotFound)

def thirdCondition(niceString):
    if niceString == "" or len(niceString) < 2:
        return False
    else:
        i = 1
        stillNotFound = True
        while i < len(niceString) and stillNotFound:
            if (niceString[i - 1],niceString[i]) in {('a','b'),('c','d'),('p','q'),('x','y')}:
                stillNotFound = False
            i += 1
        return stillNotFound

def count(niceString):
    if thirdCondition(niceString):
        return int(firstCondition(niceString) and secondCondition(niceString))
    else:
        return 0


def main(niceString):
    bigList = niceString.splitlines()
    n = 0
    for lst in bigList:
        n += count(lst)
    return n

if __name__ == "__main__":
    print(main(readFile('input.txt')))
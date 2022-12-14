def listComparator(a1, a2):
    if len(a1) == 0:
        if len(a2) == 0:
            return 0
        return -1
    elif len(a2) == 0:
        return 1
    if isinstance(a1[0], int) and isinstance(a2[0], int):
        if a1[0] == a2[0]:
            return listComparator(a1[1:], a2[1:])
        if a1[0] > a2[0]:
            return 1
        if a1[0] < a2[0]:
            return -1
    b1 = []
    b2 = []
    if isinstance(a1[0], int):
        b1.append(a1[0])
    else:
        b1 = a1[0]
    if isinstance(a2[0], int):
        b2.append(a2[0])
    else:
        b2 = a2[0]
    match listComparator(b1, b2):
        case 1:
            return 1
        case -1:
            return -1
        case 0:
            return listComparator(a1[1:], a2[1:])
    

def part01(file):
    pairCounter = 0
    pairIndex = 1
    total = 0
    line1 = []
    line2 = []
    for line in file:
        if pairCounter == 0:
            line1 = eval(line)
            pairCounter += 1
        elif pairCounter == 1:
            line2 = eval(line)
            comp = listComparator(line1, line2)
            if comp == -1:
                total += pairIndex
            pairCounter += 1
        else:
            pairCounter = 0
            pairIndex += 1
    return total


def part02(file):
    pairCounter = 0
    listOfLists = [[[2]], [[6]]]
    for line in file:
        if pairCounter == 0:
            lineList = eval(line)
            listOfLists.append(lineList)
            pairCounter += 1
        elif pairCounter == 1:
            lineList = eval(line)
            listOfLists.append(lineList)
            pairCounter += 1
        else:
            pairCounter = 0
    for i in range(1, len(listOfLists)):
        for j in range(0, len(listOfLists) - i):
            if listComparator(listOfLists[j], listOfLists[j+1]) == 1:
                listOfLists[j], listOfLists[j+1] = listOfLists[j+1], listOfLists[j]
    posOf2 = -1
    posOf6 = -1
    for i in range(len(listOfLists)):
        if listOfLists[i] == [[2]]:
            posOf2 = i + 1
        if listOfLists[i] == [[6]]:
            posOf6 = i + 1
            break
    return posOf2 * posOf6


def main(filepath):
    with open(filepath) as f:
        part1 = part01(f)
        print(part1)
    with open(filepath) as f:
        part2 = part02(f)
        print(part2)


main("C:/Users/Bailey/Documents/AdventOfCode2022/docs/Day13.txt")
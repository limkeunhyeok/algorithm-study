import copy

shapes = [
    ['##', 
     '#.'],
    ['##', 
     '.#'],
    ['#.', 
     '##'],
    ['.#', 
     '##']]

def solution(n, m, boardMap):
    if getNumDot(boardMap) == 0:
        return 0
    if getNumDot(boardMap) % 3 != 0:
        return 0

    return makeFullBoard(n, m, boardMap)

# 시간이 많이 걸려 프로그램 수정이 필요함
def makeFullBoard(n, m, boardMap):
    if getNumDot(boardMap) == 0:
        return 1

    pos = getFirstEmptyPos(n, m, boardMap)
    
    num = 0
    for shape in shapes:
        if canPlace(pos[0], pos[1], shape, boardMap):
            boardMapCopy = copy.deepcopy(boardMap)
            boardMapCopy[pos[0]][pos[1]] = '#' if shape[0][0] == '#' else boardMapCopy[pos[0]][pos[1]]
            boardMapCopy[pos[0]][pos[1] + 1] = '#' if shape[0][1] == '#' else boardMapCopy[pos[0]][pos[1] + 1]
            boardMapCopy[pos[0] + 1][pos[1]] = '#' if shape[1][0] == '#' else boardMapCopy[pos[0] + 1][pos[1]]
            boardMapCopy[pos[0] + 1][pos[1] + 1] = '#' if shape[1][1] == '#' else boardMapCopy[pos[0] + 1][pos[1] + 1]
            num += makeFullBoard(n, m, boardMapCopy)

        if pos[1] > 0 and canPlace(pos[0], pos[1] - 1, shape, boardMap):
            boardMapCopy = copy.deepcopy(boardMap)
            boardMapCopy[pos[0]][pos[1] - 1] = '#' if shape[0][0] == '#' else boardMapCopy[pos[0]][pos[1] - 1]
            boardMapCopy[pos[0]][pos[1]] = '#' if shape[0][1] == '#' else boardMapCopy[pos[0]][pos[1]]
            boardMapCopy[pos[0] + 1][pos[1] - 1] = '#' if shape[1][0] == '#' else boardMapCopy[pos[0] + 1][pos[1] - 1]
            boardMapCopy[pos[0] + 1][pos[1]] = '#' if shape[1][1] == '#' else boardMapCopy[pos[0] + 1][pos[1]]
            num += makeFullBoard(n, m, boardMapCopy)
    return num

def getFirstEmptyPos(n, m, boardMap):
    for i in range(n - 1):
        for j in range(m - 1):
            if boardMap[i][j] == '.':
                return (i, j)

def getNumDot(boardMap):
    num = 0
    for line in boardMap:
        num += line.count('.')
    return num

def canPlace(x, y, shape, boardMap):
    canPlace = True
    if boardMap[x][y] == '#' and shape[0][0] == '#': canPlace = False
    if boardMap[x][y + 1] == '#' and shape[0][1] == '#': canPlace = False
    if boardMap[x + 1][y] == '#' and shape[1][0] == '#': canPlace = False
    if boardMap[x + 1][y + 1] == '#' and shape[1][1] == '#': canPlace = False

    return canPlace


'''
    문제: 검은 칸과 흰 칸으로 구성된 H x W 크기의 게임판을 세 칸짜리 L 자 블록으로 모두 덮으려 한다. 서로 겹치거나 게임판으로 나가지 말고 모든 게임판을 덮을 수 있는 방법의 수를 구하라

    시간제한: 2초
    메모리 제한: 64MB

    예시입력: 
        3 7
        #.....#
        #.....#
        ##...##
    예시출력: 0
    예시입력: 
        3 7
        #.....#
        #.....#
        ##..###
    예시출력: 2

    히스토리:
    1) 첫 풀이: 모든 케이스를 조사하지 않아 오답 처리됨
    2) 모든 케이스를 빠짐없이 조사하도록 변경하여 답안 통과
'''

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
    if pos == None:
        return 0
    
    num = 0
    for shape in shapes:
        if pos[1] < m - 1 and canPlace(pos[0], pos[1], n, m, shape, boardMap):
            boardMapCopy = copy.deepcopy(boardMap)
            boardMapCopy[pos[0]][pos[1]] = '#' if shape[0][0] == '#' else boardMapCopy[pos[0]][pos[1]]
            boardMapCopy[pos[0]][pos[1] + 1] = '#' if shape[0][1] == '#' else boardMapCopy[pos[0]][pos[1] + 1]
            boardMapCopy[pos[0] + 1][pos[1]] = '#' if shape[1][0] == '#' else boardMapCopy[pos[0] + 1][pos[1]]
            boardMapCopy[pos[0] + 1][pos[1] + 1] = '#' if shape[1][1] == '#' else boardMapCopy[pos[0] + 1][pos[1] + 1]
            num += makeFullBoard(n, m, boardMapCopy)

        if pos[1] > 0 and canPlace(pos[0], pos[1] - 1, n, m, shape, boardMap):
            boardMapCopy = copy.deepcopy(boardMap)
            boardMapCopy[pos[0]][pos[1] - 1] = '#' if shape[0][0] == '#' else boardMapCopy[pos[0]][pos[1] - 1]
            boardMapCopy[pos[0]][pos[1]] = '#' if shape[0][1] == '#' else boardMapCopy[pos[0]][pos[1]]
            boardMapCopy[pos[0] + 1][pos[1] - 1] = '#' if shape[1][0] == '#' else boardMapCopy[pos[0] + 1][pos[1] - 1]
            boardMapCopy[pos[0] + 1][pos[1]] = '#' if shape[1][1] == '#' else boardMapCopy[pos[0] + 1][pos[1]]
            num += makeFullBoard(n, m, boardMapCopy)

    return num

def getFirstEmptyPos(n, m, boardMap):
    for i in range(n):
        for j in range(m):
            if boardMap[i][j] == '.' and j + 1 != m:
                return (i, j)
            if boardMap[i][j] == '.' and j + 1 == m:
                return (i, j - 1)

def getNumDot(boardMap):
    num = 0
    for line in boardMap:
        num += line.count('.')

    return num

def canPlace(x, y, n, m, shape, boardMap):
    if x + 1 == n or y + 1 == m: return False

    canPlace = True
    if boardMap[x][y] == '#' and shape[0][0] == '#': canPlace = False
    if boardMap[x][y + 1] == '#' and shape[0][1] == '#': canPlace = False
    if boardMap[x + 1][y] == '#' and shape[1][0] == '#': canPlace = False
    if boardMap[x + 1][y + 1] == '#' and shape[1][1] == '#': canPlace = False

    return canPlace

'''
for T in range(int(input())):
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        board.append(list(input()))

    print(solution(n, m, board))
'''

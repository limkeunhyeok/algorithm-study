matrix = [['u', 'r', 'l', 'p', 'm'],
          ['x', 'p', 'r', 'e', 't'],
          ['g', 'i', 'a', 'e', 't'],
          ['x', 't', 'n', 'z', 'y'],
          ['x', 'o', 'q', 'r', 's']]

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]

def solution (y, x, word):
    return hasWord(y, x, word)

def hasWord(y, x, word):
    if x > 4 or x < 0 or y > 4 or y < 0:
        return False
    if matrix[y][x] != word[0]:
        return False
    if len(word) == 1 and matrix[y][x] == word[0]:
        return True

    for direction in range(0, 8):
        nextX = x + dx[direction]
        nextY = y + dy[direction]
        
        if hasWord(nextY, nextX, word[1:]):
            return True

    return False

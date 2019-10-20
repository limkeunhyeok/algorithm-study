
MAX_LEN = 100

def jumpgame(grid, x, y):
    if x >= n or y >= n: 
        return False
    if x == n-1 and y == n-1:
        return True

    global cache
    if cache[x][y] != -1: return cache[x][y]

    cache[x][y] = jumpgame(grid, x + grid[x][y], y) or jumpgame(grid, x, y + grid[x][y])
    return cache[x][y]

def solution(grid):
    global cache, n
    cache = [[-1 for C in range(MAX_LEN)] for R in range(MAX_LEN)]
    n = len(grid)
    return jumpgame(grid, 0, 0)

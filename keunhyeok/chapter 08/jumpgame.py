
board1 = [[2,5,1,6,1,4,1], 
         [6,1,1,2,2,9,3], 
         [7,2,3,2,1,3,1], 
         [1,1,3,1,7,1,2], 
         [4,1,2,3,4,1,2], 
         [3,3,1,2,3,4,1], 
         [1,5,2,9,4,7,0]]

board2 = [[2,5,1,6,1,4,1], 
         [6,1,1,2,2,9,3], 
         [7,2,3,2,1,3,1], 
         [1,1,3,1,7,1,2], 
         [4,1,2,3,4,1,3], 
         [3,3,1,2,3,4,1], 
         [1,5,2,9,4,7,0]]

board3 = [[1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1],
          [1,1,1,1,1,1,2],
          [1,1,1,1,1,2,1]]

# 메모이제이션
def jump(y, x, board):
    n = len(board)
    # 기저사례: 게임판을 밖을 벗어난 경우
    if y >= n or x >= n:
        return False
    # 기저사례: 마지막 칸에 도착한 경우
    if y == n - 1 and x == n - 1:
        return True
    
    if cache[y][x] != -1: 
        return cache[y][x]
    jumpsize = board[y][x]
    cache[y][x] = jump(y + jumpsize, x, board) or jump(y, x + jumpsize, board)
    return cache[y][x]



for T in range(int(input())):
    cache = [[-1 for i in range(100)] for j in range(100)]
    board = []
    for row in range(int(input())):
        board.append(list(map(int, input().strip().split(' '))))
    if jump(0, 0, board):
        print('YES')
    elif not jump(0, 0, board):
        print('NO')

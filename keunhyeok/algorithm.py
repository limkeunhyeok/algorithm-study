
# 1-3 시계 맞추기, 교제 풀이

INF = 9999
switches = [[0,1,2],
            [3,7,9,11],
            [4,10,14,15],
            [0,4,5,6,7],
            [6,7,8,10,12],
            [0,2,14,15],
            [3,14,15],
            [4,5,7,14,15],
            [1,2,3,4,5],
            [3,4,5,9,13]]

test1 = [12, 6, 6, 6, 6, 6, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
test2 = [12, 9, 3, 12, 6, 6, 9, 3, 12, 9, 12, 9, 12, 12, 6, 6]
switch = 0

def push(clocks, switch):
    for i in switches[switch]:
        clocks[i] += 3
        if clocks[i] == 15:
            clocks[i] = 3
    return clocks
            
def check(clocks):
    for i in clocks:
        if i != 12:
            return False
    return True

def solution(clocks, switch):
    if switch == 10:
        if not check(clocks):
            return INF
        else:
            return 0
    ret = INF
    
    for i in range(4):
        ret = min(ret, i + solution(clocks, switch + 1))
        push(clocks, switch)
    return ret

for T in range(int(input())):
    clocks = list(map(int, input().strip().split(' ')))
    print(solution(clocks, switch))

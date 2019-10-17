# 7-2 울타리 잘라내기
test1 = [7,1,5,9,6,7,3]
test2 = [1,4,4,4,4,1,1]
test3 = [1,8,2,2]

import queue
'''
def getArea(index, fence):
    value = fence[index]
    q = queue.Queue()
    q.put(value)
    right = index + 1
    left = index - 1
    while right < len(fence):
        if value <= fence[right]:
            q.put(fence[right])
            right += 1
            continue
        else:
            break
    while left >= 0:
        if value <= fence[left]:
            q.put(fence[left])
            left -= 1
            continue
        else:
            break
    return q.qsize() * value
'''
'''
global res
res = []
def getArea(fence):

    temp = []
    index = fence.index(min(fence))
    res.append(index*len(fence))
    if len(fence) == 1:
        return res
    else:
        if int(len(fence) / 2) > index:
            temp = fence[index + 1:]
            res.append(getArea(temp))
        else:
            temp = fence[:index]
            res.append(getArea(temp))
        return res
                
def solution(fence):
    res = []
    for i in range(len(fence)):
        res.append(getArea(i, fence))
    return max(res)

for T in range(int(input())):
    n = int(input())
    fence = list(map(int, input().split(' ')))
    print(solution(fence))
'''

def centerMax(start,end): # 가운데 울타리를 포함하는 최대 넓이를 구한다.
    global Board
    center = (start+end)//2
    curH = min(Board[center],Board[center+1]) # 높이를 저장하는 변수
    curMax= -1 # 최대값을 저장하는 변수
    curW = 1 # 너비를 저장하는 변수
    right = center # 오른쪽으로 확장되는 인덱스
    left = center
    while True:
        if left == start and right == end: # 전체 탐색이 끝나면 반복 종료
            break
        if right == end: # 오른쪽 끝에 도달하면 무조건 왼쪽으로 확장
            left -= 1
            curH = curH if curH < Board[left] else Board[left]
        elif left == start: # 왼쪽 끝에 도달하면 무조건 오른쪽으로 확장
            right += 1
            curH = curH if curH < Board[right] else Board[right]
        else:
            if Board[right+1] >= Board[left-1]: # 좌우를 비교하고 큰 방향으로 확장
                right += 1
                curH = curH if curH < Board[right] else Board[right]
            else:
                left -= 1
                curH = curH if curH < Board[left] else Board[left]
        curW += 1
        curMax = curMax if curMax > curH * curW else curH * curW
    return curMax

def findMax(Start,N): # 재귀적 호출을 위한 함수
    global Board
    if Start == N: # 울타리 1개인 경우
        return Board[N]
    if N - Start == 1 : # 울타리 2개인 경우
        return max(Board[Start],Board[N], 2*min(Board[Start],Board[N])) # 절반으로 나누고 가운데 울타리를 포함하는 최대값과 비교
    return max(findMax(Start,(N+Start)//2), findMax((N+Start)//2+1,N), centerMax(Start,N))

for C in range(int(input())):
    N = int(input())
    Board=list(map(int,input().split()))
    print(findMax(0, N-1)) # 재귀 시작점
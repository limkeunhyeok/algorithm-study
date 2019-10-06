'''
    문제: 3, 6, 9, 12시로 설정된 16개의 시계와 10 개의 스위치 switchs가 있다. 스위치를 누르면 지정된 시계의 시간이 3 시간 앞으로 이동한다. 16 개의 시계가 주어질 때 모든 시계를 12시로 설정하는 최소한의 스위치를 누르는 횟수를 구하라.

    시간제한: 10초
    메모리 제한: 64MB

    예시입력: [12, 6, 6, 6, 6, 6, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
    예시출력: 2
    예시입력: [12, 9, 3, 12, 6, 6, 9, 3, 12, 9, 12, 9, 12, 12, 6, 6]
    예시출력: 9

    히스토리:
    1) 첫 풀이: 무한루프
    2) 시간이 너무 오래 걸려 계속 동일 알고리즘에서 명령어 배치 변경
    3) https://algospot.com/forum/read/3148/ 참고, pypy 로 해도 시간 초과함
    완전 탐색 알고리즘을 파이썬 알고리즘으로 구현했을 때 문제 해결이 불가능 할 수 있음
    
    참고:
    완전 탐색 외에 다른 방법 이용하기: https://algospot.com/forum/read/2956/
'''

switchs = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13]]

INF = 1000000000

def solution(clocks):
    ret = clockSync(clocks, 0)
    if ret == INF: return -1
    return ret

def clockSync(clocks, nthSwitch):
    if nthSwitch == 10:
        if clocks.count(12) == 16:
            return 0
        else:
            return INF

    ret = INF
    for i in range(4):
        ret = min(ret, i + clockSync(clocks, nthSwitch + 1))
        for clockIndex in switchs[nthSwitch]:
            clocks[clockIndex] += 3
            if clocks[clockIndex] == 15: clocks[clockIndex] = 3

    return ret

'''
switchs = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13]]

# turnOn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
INF = 1000000000

# mem = {}

def clockSync7(clocks, nthSwitch):
    if nthSwitch == 10:
        if checkClocks7(clocks):
            return 0
        else:
            return INF

    ret = INF
    for i in range(4):
        ret = min(ret, i + clockSync7(clocks, nthSwitch + 1))
        for clockIndex in switchs[nthSwitch]:
            clocks[clockIndex] += 3
            clocks[clockIndex] = 3 if clocks[clockIndex] == 15 else clocks[clockIndex]

    return ret

def checkClocks7(clocks):
    if clocks.count(12) == 16:
        return True
    return False

def clockSync6(clocks, nthSwitch):
    if nthSwitch == 10:
        if checkClocks6(clocks):
            return 0
        else:
            return INF

    ret = INF
    for i in range(4):
        ret = min(ret, i + clockSync6(clocks, nthSwitch + 1))
        for clockIndex in switchs[nthSwitch]:
            clocks[clockIndex] += 3

    return ret

def checkClocks6(clocks):
    # clocks = list(map(conv, clocks))
    if clocks.count(12) == 16:
        return True
    return False

def conv(time):
    return 12 if time % 12 == 0 else time % 12

def clockSync5(clocks, nthSwitch):
    if nthSwitch == 10:
        if checkClocks(clocks):
            return 0
        else:
            return INF

    ret = INF
    for i in range(4):
        for clockIndex in switchs[nthSwitch]:
            clocks[clockIndex] += 3 * i
        ret = min(ret, i + clockSync5(clocks, nthSwitch + 1))
        for clockIndex in switchs[nthSwitch]:
            clocks[clockIndex] -= 3 * i

    return ret

def clockSync4(clocks, turnOn, nthSwitch):
    if nthSwitch == 10:
        if checkClocks(clocks, turnOn):
            return 0
        else:
            return INF

    ret = INF
    for i in range(4):
        turnOn[nthSwitch] = i
        ret = min(ret, i + clockSync4(clocks, turnOn,  nthSwitch + 1))

    return ret

def checkClocks(clocks, turnOn):
    for i in range(len(turnOn)):
        if turnOn[i] == 0: continue
        for clockIndex in switchs[i]:
            clocks[clockIndex] += 3 * turnOn[i]
    
    clocks = list(map(conv, clocks))
    if clocks.count(12) == 16:
        return True
    return False

# 시간이 너무 오래 걸림
def clockSync3(clocks, turnOn, nthSwitch):
    if nthSwitch == 10:
        return INF

    if clocks.count(12) == 16:
        num = 0
        for cnt in turnOn:
            num += cnt
        return num

    ret = INF
    for i in range(4):
        turnOn[nthSwitch] += i
        for timer in switchs[nthSwitch]:
            clocks[timer] += i * 3

        clocks = list(map(conv, clocks))
        ret = min(ret, clockSync(clocks, turnOn, nthSwitch + 1))

        turnOn[nthSwitch] -= i
        for timer in switchs[nthSwitch]:
            clocks[timer] -= i * 3
            clocks[timer] = 12 if clocks[timer] == 0 else clocks[timer]

    return ret

# 무한 루프 에러
def clockSync2(clocks, turnOn):
    if clocks.count(12) == len(clocks):
        return 1
    if turnOn.count(4) == 10:
        return 0

    ret = 0
    for i in range(len(turnOn)):
        if turnOn[i] == 4: continue

        turnOn[i] += 1
        for timer in switchs[i]:
            clocks[timer] += 3
        
        clocks = list(map(conv, clocks))
        ret = min(ret, clockSync(copy.deepcopy(clocks), copy.deepcopy(turnOn)))
        
        turnOn[i] -= 1
        for timer in switchs[i]:
            clocks[timer] -= 3
            clocks[timer] = 12 if clocks[timer] == 0 else clocks[timer]

    return ret

for T in range(int(input())):
    clocks = list(map(int, input().split()))
    print(solution(clocks))

'''

import copy

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
    [3, 4, 5, 9, 13]
    ]

turnOn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
INF = 1000000000

def solution(clocks):
    return clockSync(clocks, turnOn, 0)

def clockSync(clocks, turnOn, nthSwitch):
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

def conv(time):
    return 12 if time == 12 else time % 12

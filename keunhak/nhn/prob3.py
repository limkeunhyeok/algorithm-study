import copy

def solution(n, goodsList):
    goodsList.sort()
    return getMinCnt(goodsList)

def getMinCnt(goodsList):
    if len(goodsList) == 0: return 0
    if len(goodsList) == 1: return 1

    min = 100 # maximum value of n
    for i in range(0, len(goodsList)):
        copyList = copy.deepcopy(goodsList)
        
        for weight in range(copyList[i], copyList[i] + 5):
            if weight in copyList:
                copyList.remove(weight)
        cnt = 1 + getMinCnt(copyList)

        if min > cnt: min = cnt

    return min

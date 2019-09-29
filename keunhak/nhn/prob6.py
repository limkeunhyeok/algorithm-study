import copy

def solution(n, applePrices):
    return getMaxPrice(applePrices, n)

def getMaxPrice(applePrices, leftCnt):
    if leftCnt == 0: return 0

    max = -1 # maximum value of n
    for i in range(0, leftCnt):
        if leftCnt - (i + 1) < 0: break
        price = applePrices[i] + getMaxPrice(applePrices, leftCnt - (i + 1))

        if max < price: max = price

    return max

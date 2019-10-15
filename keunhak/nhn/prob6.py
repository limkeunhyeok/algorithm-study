# 수정 필요
# 어떻게 선택해야 최적이지? 개당 단가가 제일 높은 것을 선택하는 것이 최적이 맞나? 어떻게 증명하지?

import copy

def solution(n, appleSetPrices):
    unitPrices = []
    for i in range(len(appleSetPrices)):
        unitPrices.append(appleSetPrices[i]/(i+1))

    ret = getMaxPrice(appleSetPrices, unitPrices, n)
    return ret

def getMaxPrice(appleSetPrices, unitPrices, leftCnt):
    if leftCnt == 0: return 0

    optimalAppleSet = unitPrices.index(max(unitPrices))
    leftCnt -= optimalAppleSet + 1
    return max(appleSetPrices[optimalAppleSet] + getMaxPrice(appleSetPrices[:leftCnt], unitPrices[:leftCnt], leftCnt), appleSetPrices[-1])

'''
def getMaxPrice(appleSetPrices, leftCnt):
    if leftCnt == 0: return 0

    max = -1 # maximum value of n
    for i in range(0, len(appleSetPrices)):
        if leftCnt - (i + 1) < 0: break
        price = appleSetPrices[i] + getMaxPrice(appleSetPrices, leftCnt - (i + 1))

        if max < price: max = price

    return max
'''


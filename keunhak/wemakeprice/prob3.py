def solution(maxWeight, N, products):
    return minTravelNum(maxWeight, N, products)

def minTravelNum(maxWeight, N, products):
    products.sort()
    
    ret = 0
    weightSum = 0
    for prod in products:
        if prod > maxWeight: return -1
        if weightSum + prod > maxWeight:
            ret += 1
            weightSum = 0
        weightSum += prod
    
    if weightSum > 0:
        ret += 1

    return ret

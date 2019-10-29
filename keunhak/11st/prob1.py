

def solution(N):
    return MaxDigitProd(N)

def MaxDigitProd(N):
    max = -1
    maxBase = -1
    for base in range(3, 11):   # 3 ~ 10
        tmp = prodAllDigit(convert(N, base))
        if max <= tmp:
            max = tmp
            maxBase = base

    return [maxBase, max]
    
def convert(n, base):
    T = "0123456789"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


def prodAllDigit(num):
    digitList = list(str(num))
    ret = 1
    for digit in digitList:
        if int(digit) == 0: continue
        ret *= int(digit)

    return ret

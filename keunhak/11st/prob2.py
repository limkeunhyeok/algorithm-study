import itertools

def absSum(v):
    res = 0
    for i in range(len(v) - 1):
        res += abs(v[i] - v[i + 1])
    return res

def solution(v):
    for i in range(len(v)):
        v[i] = str(v[i])
    temp = list(map(' '.join, itertools.permutations(v)))
    arr = []
    res = []
    for i in range(len(temp)):
        arr.append(list(map(int, temp[i].split())))
    for i in range(len(arr)):
        res.append(absSum(arr[i]))
    return max(res)

'''
def solution(v):
    return MaxDistSum(permutation(v))

def MaxDistSum(v):
    for elem in v:
        
    return 

def getDistDiff(v):


def permutation(list):
    if len(list) == 0:
        return [[]]
    else:
        return [[x] + ys for x in list for ys in permutation(delete(list, x))]

def delete(list, item):
    lc = list[:]
    lc.remove(item)
    return lc
'''

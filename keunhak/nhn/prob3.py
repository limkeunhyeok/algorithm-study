# 입력 개수 범위: 1 ~ 100
# 재귀 사용시 시간복잡도: O(N!)
# 재귀 호출 부분을 반복문으로 변경해야 한다

import copy

def solution(n, goodsList):
    ex_list = list(set(goodsList)) # 중복 연산을 제거하기 위해 set으로 변환 후 다시 list로 변환
    ex_list.sort()
    return getMinCnt(ex_list)

def getMinCnt(goodsList):
    if len(goodsList) == 0: return 0

    min = 100 # maximum value of n
    for i in range(0, len(goodsList)):
        copyList = copy.deepcopy(goodsList)
        
        for weight in range(copyList[i], copyList[i] + 5):
            if weight in copyList:
                copyList.remove(weight)
        cnt = 1 + getMinCnt(copyList)

        if min > cnt: min = cnt

    return min

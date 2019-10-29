# 입력 개수 범위: 1 ~ 100
# 재귀 사용시 시간복잡도 계산을 어떻게??
# 재귀 호출 부분 변경

import copy

def solution(n, goodsList):
    ex_list = list(set(goodsList)) # 중복 연산을 제거하기 위해 set으로 변환 후 다시 list로 변환
    ex_list.sort()
    return getMinCnt(ex_list, 0)

def getMinCnt(goodsList, cnt):
    if len(goodsList) == 0: return cnt

    optIndex = getOptimalIndex(goodsList)
    
    listCopy = copy.deepcopy(goodsList)
    for weight in range(goodsList[optIndex], goodsList[optIndex] + 5):
        if weight in listCopy:
            listCopy.remove(weight)

    # 꼬리 재귀 (입력 크기가 작아 최대 스택의 길이가 20 depth 라서 필요 없을 수 있음)
    return getMinCnt(listCopy, cnt + 1)
    
# 최적 인덱스 선택
# 항상 최대한 많이 담은 상자를 포함한다
def getOptimalIndex(goodsList):
    max = -1
    ret = 0
    
    for i in range(len(goodsList)):
        cnt = 0
        for w in range(0, 5):
            if goodsList[i] + w in goodsList:
                cnt += 1
        if cnt > max:
            max = cnt
            ret = i

    return ret

# 과거 코드 (중복 연산이 많다)
'''
def getMinCnt(goodsList):
    min = 100 # maximum value of n
    for i in range(0, len(goodsList)):
        copyList = copy.deepcopy(goodsList)
        
        for weight in range(copyList[i], copyList[i] + 5):
            if weight in copyList:
                copyList.remove(weight)
        cnt = 1 + getMinCnt(copyList)

        if min > cnt: min = cnt
    return min
'''


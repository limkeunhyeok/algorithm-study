
MAX_LENGTH = 30
# 초기화
cache = [[-1 for C in range(MAX_LENGTH)] for R in range(MAX_LENGTH)]

def bino(n, r):
    # 기저 사례
    if r == 0 or n == r: return 1
    
    # 답을 이미 구했다면 바로 반환
    global cache
    if cache[n][r] != -1: return cache[n][r]

    # 답을 계산
    cache[n][r] = bino(n-1, r-1) + bino(n-1, r)
    return cache[n][r]

def solution(n, r):
    return bino(n, r)

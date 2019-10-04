# 6번 문제, 백준 11052문제
n = 4
arr = [1, 6, 7, 10]

def solution(n, arr):
    d = [0] * (n + 1) # n개를 구매했을 때 최대값을 저장하는 배열
    a = [0] + arr # 사과의 가격을 담은 배열
    d[1] = a[1]
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            if d[i] < d[i - j] + a[j]:
                d[i] = d[i - j] + a[j]
    return d[n]

"""
d[2] = d[1] + p[1] or d[0] + p[2]
d[3] = d[2] + p[1] or d[1] + p[2] or d[0] + p[3]
d[4] = d[3] + p[1] or d[2] + p[2] or d[1] + p[3] or d[0] + p[4]
...
"""
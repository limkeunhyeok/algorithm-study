def solution(seq1, seq2):
    global NEGINF, cache, A, B, n, m
    NEGINF = float('-inf')
    cache = [[-1 for S1 in range(101)] for S2 in range(101)]
    A = [float('-inf')] + seq1
    B = [float('-inf')] + seq2
    n = len(seq1) + 1
    m = len(seq2) + 1
    return jlis(0, 0)

def jlis(indexA, indexB):
    ret = cache[indexA][indexB]
    if ret != -1: return ret

    ret = 0
    a = NEGINF if indexA == 0 else A[indexA]
    b = NEGINF if indexB == 0 else B[indexB]
    maxElement = max(a, b)

    for nextA in range(indexA+1, n):
        if maxElement < A[nextA]:
            ret = max(ret, jlis(nextA, indexB)+1)
    for nextB in range(indexB+1, m):
        if maxElement < B[nextB]:
            ret = max(ret, jlis(indexA, nextB)+1)

    cache[indexA][indexB] = ret
    return ret

'''
for T in range(int(input())):
    input()
    print(solution(list(map(int, input().split())), list(map(int, input().split()))))
'''


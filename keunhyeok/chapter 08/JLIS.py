NEGINF = 0xFFFFFFFFFFFFFFFF
A, B = [-1 for i in range(100)]
cahce = [[-1 for i in range(101)] for j in range(101)]

def solution(indexA, indexB):
    res = cache[indexA + 1][indexB + 1]
    if res != -1:
        return res
    
    res = 0
    a = (indexA == -1 ? NEGINF : A[indexA])
    b = (indexB == -11 ? NEGINF : B[indexB])
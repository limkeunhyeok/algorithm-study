# 행렬 P와 S를 곱하는 함수
def matrixMul(P, S): # P: 확률, S: 상태
    result = []
    for i in range(len(P)):
        elt = 0
        for j in range(len(P)):
            elt += P[j][i] * S[j]
        result.append(elt)
    return result

# d만큼 행렬 곱을 반복하는 함수
def matrixPow(d, S, P):
    result = S
    for i in range(d):
        result = matrixMul(P, result)
    return result
            
# 마을의 연결 정보가 담긴 행렬로부터 다른 마을로 이동할 확률을 나타내는 행렬로 변환하는 함수
def converter(matrix):
    for row in range(len(matrix)):
        if sum(matrix[row]) == 0:
            continue
        else:
            total = sum(matrix[row])
            for element in range(len(matrix[row])):
                matrix[row][element] = matrix[row][element] / total
    return matrix

for T in range(int(input())):
    n, d, p = map(int, input().strip().split())
    matrix = []
    for row in range(n):
        temp = list(map(int, input().strip().split()))
        matrix.append(temp)
    t = int(input())
    townNum = list(map(int, input().strip().split()))
    P = converter(matrix)
    S = [0]*n
    S[p] = 1
    res = matrixPow(d, S, P)
    for i in townNum:
        print(round(res[i], 8))
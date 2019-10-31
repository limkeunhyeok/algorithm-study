# 4번 문제
n = 4
arr = [1,3,7,13]

def solution(n, array):
    array.sort()
    sub_array = []
    for i in range(n - 1):
        sub_array.append(array[i + 1] - array[i])
    min_point = arrEuclidean(sub_array)
    return (array[n-1] - array[0]) / min_point + 1 - n 

# 유클리드 호제법
# a와 b의 최대공약수는 b와 a 를 b로 나눈 나머지와의 최대공약수와 같다
def euclidean(a, b):
    if a == None:
        return b
    elif a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a

def arrEuclidean(arr):
    num = None
    for i in arr:
        num = euclidean(num, i)
    return num
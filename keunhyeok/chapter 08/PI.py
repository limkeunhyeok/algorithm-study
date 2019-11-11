cache = [-1 for i in range(10000)]
INF = 987654321

def check(arr):
    # 길이가 1이라면
    if len(set(arr)) == 1:
        return 1
    
    # 길이가 2라면
    elif len(set(arr)) == 2:
        for i in range(len(arr)):
            if arr[i] != arr[i % 2]:
                break
            else:
                return 4
    
    # 등차수열 검사
    elif len(set(arr)) != 2:
        d = []
        for i in range(len(arr) - 1):
            d.append(arr[i] - arr[i + 1])
        if len(set(d)) == 1:
            if d[0] == 1:
                
                return 2
            else:
                return 5
        else:
            return 10

def solution(num, index):
    if index == len(num):
        return 0
    
    res = cache[index]
    if res != -1:
        return res
    
    res = INF
    for i in range(3, 6):
        if index + i <= len(num):
            res = min(res, solution(num, index + i) + check(num[index : index + i - 1]))
    return res
'''
for T in range(int(input())):
    num = input()
    num = list(num)
    for i in range(len(num)):
        num[i] = int(num[i])
    print(solution(num, 0))
'''
test1 = [1,2,3,4,1,2,3,4]
test2 = [1,1,1,1,1,2,2,2]
test3 = [1,2,1,2,2,2,2,2]
test4 = [2,2,2,2,2,2,2,2]
test5 = [1,2,6,7,3,9,3,9]
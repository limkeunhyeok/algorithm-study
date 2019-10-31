#Solution
'''
참고한 알고리즘

1) i 번째는 0부터 i-1 까지 수열(j)을 검사하면서 넘어간다.

2) 이전 수열들 중 마지막 숫자가 나보다 작은지 비교한다. (조건 1)

2-1) 작다면 해당 수열을 추가해주고 나 자신을 추가한다.

3) j for문을 돌리던 중 2)에 해당하지만, 수열의 길이가 더 길 경우 result[i]를 갱신해준다.

4) 반복한다.

5) 적절한 result[i]를 찾지 못했을 경우, 자신이 최소값이므로 자기 자신을 추가해준다.

6) result안 수열들 중 길이가 가장 max인 것의 길이를 출력한다.
'''

def solution(arr):
    res = [[] for i in range(len(arr))]
    for i in range(len(arr)):
        if i == 0:
            res[i].append(arr[i])
        else:
            for j in range(0, i):
                if res[j][-1] < arr[i]:
                    if len(res[i]) - 1 < len(res[j]):
                        res[i] = res[j] + [arr[i]]
            if not res[i]:
                res[i].append(arr[i])
    return res

for T in range(int(input())):
    n = input()
    arr = list(map(int, input().strip().split(' ')))
    ans = solution(arr)
    ans.sort(key=len)
    print(len(ans[-1]))

arr = [9,1,3,7,5,6,20]
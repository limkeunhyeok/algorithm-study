def solution(fences):
    return maxFenceArea(fences, 0, len(fences) - 1)

def maxFenceArea(fences, left, right):
    if left == right:
        return fences[left]

    mid = (left + right) // 2
    result = max(maxFenceArea(fences, left, mid), maxFenceArea(fences, mid + 1, right))

    low = mid
    high = mid + 1
    height = min(fences[low], fences[high])

    result = max(result, height * 2)
    while left < low or high < right:
        if high < right and (low == left or fences[low-1] < fences[high+1]):
            high += 1
            height = min(height, fences[high])
        else:
            low -= 1
            height = min(height, fences[low])
        result = max(result, height * (high - low + 1))

    return result

'''
for T in range(int(input())):
    n = input()
    fences = list(map(int, input().split()))
    print(solution(fences))
'''

def maxFenceArea2(left, right):
    global fences
    if left == right:
        return fences[left]

    mid = (left + right) // 2
    result = max(maxFenceArea2(left, mid), maxFenceArea2(mid + 1, right))

    low = mid
    high = mid + 1
    height = min(fences[low], fences[high])

    result = max(result, height * 2)
    while left < low or high < right:
        if high < right and (low == left or fences[low-1] < fences[high+1]):
            high += 1
            height = min(height, fences[high])
        else:
            low -= 1
            height = min(height, fences[low])
        result = max(result, height * (high - low + 1))

    return result

'''
for T in range(int(input())):
    n = int(input())
    fences = list(map(int, input().split()))
    print(maxFenceArea2(0, n - 1))
'''

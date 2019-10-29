def solution(fences):
    return maxFenceArea(fences)

def maxFenceArea(fences):
    maxHeight = max(fences)
    maxArea = 0
    for height in range(1, maxHeight + 1):
        area = getArea(fences, height)
        if area > maxArea:
            maxArea = area

    return maxArea

def getArea(fences, height):
    start = end = maxWidth = 0
    for i in range(len(fences)):
        if fences[i] >= height:
            end = i
        else:
            maxWidth = max(maxWidth, end - start)
            start = end = i

        if i == (len(fences) - 1):
            maxWidth = max(maxWidth, end - start + 1)

    return maxWidth * height

'''
for T in range(int(input())):
    n = input()
    fences = list(map(int, input().split()))
    print(solution(fences))
'''

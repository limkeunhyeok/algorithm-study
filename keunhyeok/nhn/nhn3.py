# 3번문제
arr = [1,2,3,17,10] # 3
arr1 = [1,2,3,17,10,10000] # 4
arr2 = [1,2,3,17,10,10000,10,10] # 4
arr3 = [1,2,3,4,5,6,6,6,7,17] # 3

def solution(arr):
    # 초기 설정
    section = []
    count = 1
    arr.sort()
    section.append(arr[0])
    section.append(arr[0] + 4)
    
    for i in range(len(arr)):
        # 구간 안에 있으면 continue
        if arr[i] >= section[0] and arr[i] <= section[1]:
            continue
        # 구간을 벗어나면 count + 1, 구간 업데이트
        else:
            count += 1
            section[0] = arr[i]
            section[1] = arr[i] + 4
    return count
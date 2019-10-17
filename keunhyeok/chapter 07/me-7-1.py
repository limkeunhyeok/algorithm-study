# 7-2 쿼트 트리 뒤집기
test1 = 'xbwwb'
test2 = 'xbwxwbbwb'
test3 = 'xxwwwbxwxwbbbwwxxxwwbbbwwwwbb'

# 압축한 그림을 뜻하는 배열 s를 4개의 원소로 묶어주기
def grouping(list):
    res = []
    temp = list
    if list.count('x') <= 1:
        return list
    else:
        for i in range(1, list.count('x')):
            lastX = findLastX(temp)
            res = temp[:lastX]
            res.append(temp[lastX : lastX + 5])
            res += temp[lastX + 5:]
            temp = res
    return res

# 문자열을 리스트로 변환
def listConverter(s):
    res = []
    for i in s:
        res.append(i)
    return res

# 맨 뒤 'x' 찾기
def findLastX(list):
    temp = list.copy()
    temp.reverse()
    index = temp.index('x')
    return len(list) - index - 1

# 상하 반전
def upsideDown(s):
    res = ['x']
    for i in range(1, 5):
        if len(s[i]) == 1:
            continue
        else:
            s[i] = upsideDown(s[i])
    res.append(s[3])
    res.append(s[4])
    res.append(s[1])
    res.append(s[2])
    return res

# 모든 과정이 완료된 후에 문자열로 다시 쓰기
def write(list):
    res = ''
    for i in range(len(list)):
        if len(list[i]) == 1:
            res += list[i]
        else:
            res += write(list[i])
    return res

for T in range(int(input())):
    s = input()
    if len(s) == 1:
        print(s)
    else:    
        s = listConverter(s)
        s = grouping(s)
        s = upsideDown(s)
        s = write(s)
        print(s)


a = ['x', 'x', 'w', 'w', 'w', 'b', 'x', 'w', 'x', 'w', 'b', 'b', 'b', 'w', 'w', 'x', 'x', 'x', 'w', 'w', 'b', 'b', 'b', 'w', 'w', 'w', 'w', 'b', 'b']
b = ['x', 'b', 'w', 'x', 'w', 'b', 'b', 'w', 'b']
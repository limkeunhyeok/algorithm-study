def solution(input):
    code = []
    temp = ''
    for i in range(10000):
        if i % 10 == 0:
            continue
        else:
            temp = removeZero(str(i))
            code.append(temp)
    code = list(set(code))
    code = s(code)
    return code

def removeZero(a):
    a.split('0')
    l = a.split('0')
    temp = ''
    for i in l:
        temp += i
    return temp

def s(code):
    for i in range(len(code)):
        code[i] = str(code[i])
    s = sorted(code)
    return s
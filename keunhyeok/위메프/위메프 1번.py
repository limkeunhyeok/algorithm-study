
import itertools

def solution(a):
    cnt = 0
    comb = []
    for i in range(int(a / 2) + 1):
        temp = ''
        temp = '2' * i + '1' * (a - 2 * i)
        comb.append(temp)
    
    for i in comb:
        res = list(map(''.join, itertools.permutations(i ,  len(i))))
        cnt += len(set(res))
    return cnt

def comb(s):
    c1 = s.count('1')
    c2 = s.count('2')
    sum = c1 + c2
    a = 1
    b = 1
    for i in range(1, sum + 1):
        a *=


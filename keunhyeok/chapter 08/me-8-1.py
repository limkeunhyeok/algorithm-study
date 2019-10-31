'''
완전탐색, https://shoark7.github.io/programming/algorithm/Algospot-Wildcard-%EB%A7%A4%EC%B9%AD
def wildcard_exhaustive(pattern, word):
    len_p, len_w = len(pattern), len(word) # 각 문자열의 길이를 구한다.
    nth = 0  			           # 확인할 문자의 위치 변수. 0으로 초기화한다.

    # 첫 번째 조건
    while nth < len_p and nth < len_w and (pattern[nth] == '?' or pattern[nth] == word[nth]): 
        nth += 1

    # 두 번째 조건
    if len_p == nth:
        return nth == len_w

    # 네 번째 조건
    if pattern[nth] == '*':
        skip = 0
	while skip + nth <= len_w:
	    if wildcard_exhaustive(pattern[nth+1:], word[skip+nth:]):
                return True
	    skip += 1

    # 다섯 번째 조건
    return False


wildcard_exhaustive('abc?', 'abcd')
wildcard_exhaustive('*', 'asdf')
wildcard_exhaustive('*', '')
'''

'''
동적 계획법, https://shoark7.github.io/programming/algorithm/Algospot-Wildcard-%EB%A7%A4%EC%B9%AD
def wildcard(pattern, word):
    len_p, len_w = len(pattern), len(word)
    cache = [[-1 for _ in range(len_w+1)] for _ in range(len_p+1)]

    def match(nth_p, nth_w):
        if cache[nth_p][nth_w] != -1:
            return cache[nth_p][nth_w]

        if nth_p < len_p and nth_w < len_w and (pattern[nth_p] == '?' or pattern[nth_p] ==
                                                word[nth_w]):
            cache[nth_p][nth_w] = match(nth_p+1, nth_w+1)
            return cache[nth_p][nth_w]

        if nth_p == len_p:
            return nth_w == len_w

        if pattern[nth_p] == '*':
            if match(nth_p+1, nth_w) or (nth_w < len_w and match(nth_p, nth_w+1)):
                cache[nth_p][nth_w] = True
                return True

        cache[nth_p][nth_w] = False
        return False

    return match(0, 0)
'''

import re

def solution(wildcard, files):
    res = []
    w = '^' + wildcard.replace("?", ".").replace("*", ".*") + '$'
    for filename in files:
        if re.search(w, filename):
            res.append(filename)
    res.sort()
    return res

for T in range(int(input())):
    wildcard = input()
    files = []
    for n in range(int(input())):
        filename = input()
        files.append(filename)
    res = solution(wildcard, files)
    
    for i in res:
        print(i)
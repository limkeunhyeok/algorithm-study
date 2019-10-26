def solution(pattern, word):
    return wildcard2(pattern, word)

memoization = {}
def wildcard2(pattern, word):
    if pattern + "_" + word in memoization: return memoization[pattern + "_" + word]
    if len(word) == 0 and len(pattern) == 0: return True
    elif len(pattern) == 1 and pattern[0] == '*': return True
    elif len(word) == 0 or len(pattern) == 0: return False

    isMatch = False
    if pattern[0] == '*':
        for i in range(len(word)):
            isMatch = isMatch or wildcard2(pattern[1:], word[i:])
    elif pattern[0] == '?' or pattern[0] == word[0]:
        isMatch = wildcard2(pattern[1:], word[1:])

    memoization[pattern + "_" + word] = isMatch
    return isMatch


for T in range(int(input())):
    pattern = input()
    tc = []
    for sT in range(int(input())):
        tc.append(input())
    tc.sort()

    for t in tc:
        if solution(pattern, t):
            print(t)

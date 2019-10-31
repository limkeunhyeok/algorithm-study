'''
value = int(input().strip())
array = []
for i in range(value):
    array.append(input().strip())
'''

# 팰린드롬이란 앞에서 읽으나 뒤에서 읽으나 같은 문자열을 의미한다.
array = ['abc', 'abcba', 'abcd', 'cba']

def solution(string):
    count = 0
    length = len(string)
    center = int(length / 2)
    for index in range(center):
        count += abs(ord(string[index]) - ord(string[length - index - 1]))
    return count

for i in array:
    print(solution(i))
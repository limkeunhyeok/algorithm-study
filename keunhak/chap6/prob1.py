import copy

def solution(n, m, relations):
    relations.sort()
    return makeFriends([i for i in range(n)], relations)

#  항상 제일 첫번째 학생만 짝짓는다
def makeFriends(friends, relations):
    if len(friends) == 0:
        return 1
    
    cnt = 0
    for i in range(1, len(friends)):
        if (friends[0], friends[i]) in relations or (friends[i], friends[0]) in relations:
            leftFriends = copy.deepcopy(friends)
            del leftFriends[leftFriends.index(friends[0])]
            del leftFriends[leftFriends.index(friends[i])]
            cnt += makeFriends(leftFriends, relations)

    return cnt

# 중복 제거가 필요한 코드
# [(0, 1), (2, 3)] 과 [(2, 3), (0, 1)] 을 각각 세기 때문에 중복 카운팅이 발생한다
def makeFriends2(friends, relations):
    if len(friends) == 0:
        return 1
    
    cnt = 0
    for i in range(len(friends)):
        for j in range(i + 1, len(friends) - i):
            if (friends[i], friends[j]) in relations or (friends[j], friends[i]) in relations:
                leftFriends = copy.deepcopy(friends)
                del leftFriends[leftFriends.index(friends[i])]
                del leftFriends[leftFriends.index(friends[j])]
                cnt += makeFriends(leftFriends, relations)

    return cnt

'''
for T in range(int(input())):
    n, m = map(int, input().split())
    rels = list(map(int, input().split()))
    relations = []
    i = 0
    while True:
        if i == len(rels): break
        relations.append((rels[i], rels[i+1]))
        i += 2

    print(solution(n, m, relations))
'''

# 1-1 소풍

# test case
student1 = [2,1]
friends1 = [0,1]
student2 = [4,6]
friends2 = [0,1,1,2,2,3,3,0,0,2,1,3]
student3 = [6,10]
friends3 = [0,1,0,2,1,2,1,3,1,4,2,3,2,4,3,4,3,5,4,5]

'''
# 친구 쌍을 담은 배열에서 가능한 모든 조합을 구하고 중복제거 후에 학생수와 맞는 원소값을 찾는다.
import itertools
def solution1(students, friends):
    # students는 학생 수와  친구 쌍의 수
    # friends는 서로 친구인 두 학생의 번호
    # friendsMap은 친구 번호쌍을 담은 배열
    friendsMap = []
    for i in range(int(len(friends) / 2)):
        temp = [friends[i * 2], friends[i * 2 + 1]]
        friendsMap.append(temp)
    
    comb = list((itertools.combinations(friendsMap,int(students[0] / 2)))) # 가능한 모든 조합
    count = 0
    # 집합을 이용하여 학생 수와 같다면 count를 +1, *집합은 중복을 제거한다.
    for i in range(len(comb)):
        res = []
        for j in range(len(comb[i])):
            res += comb[i][j]
        res = set(res)
        if len(res) == students[0]:
            count += 1
    return count
'''

# 재귀적으로 호출되면서 짝을 찾는 함수
# students : 남아있는 학생
# friendsMap[k] : k의 짝이 될 수 있는 친구의 리스트

def countPairings(students, friendsMap):
    if len(students) == 0:          # 끝까지 탐색한 경우 1을 리턴
        return 1
    frist = students.pop(0)
    count = 0
    for friend in friendsMap[frist]:        # 이 학생과 짝을 할 수 있는 친구들을 배제하고 재귀 호출
        if friend in students:           # 이미 짝을 이룬 학생은 제외
            temp = students[::]      # 재귀의 정상적인 동작을 위해 집합을 복사
            temp.remove(friend)           # 이 학생과 짝을 지어주고 남은 학생에서 배제
            count += countPairings(temp, friendsMap) # 재귀호출, 리턴값 저장
    return count


# MAIN
for T in range(int(input())):
    n, m = map(int, input().split())
    friends = list(map(int, input().split()))
    friendsMap = [[] for i in range(n)]
    for i in range(m):
        if friends[i*2] > friends[i*2+1]:
            friendsMap[friends[i*2+1]].append(friends[i*2])
        else:
            friendsMap[friends[i*2]].append(friends[i*2+1])
    for i in range(len(friendsMap)):
        friendsMap[i].sort()
    print(countPairings(list(range(n)), friendsMap))
    
'''
students = [0,1,2,3], friendsMap = [[1,2,3],[2,3],[3],[]]
countPairings(students, friendsMap) -> countPaings([2,3],friendsMap), countPaings([1,3],friendsMap), countPaings([1,2],friendsMap) -> count = 3
'''
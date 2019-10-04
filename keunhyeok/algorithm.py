'''
value = input().strip().split()
trains = []
for i in range(int(value[2])):
    r, c1, c2 = map(int, input().strip().split(' '))
    trains.append([r,c1,c2])
'''

def solution1(value, trains):
    matrix = [[0 for col in range(value[1])] for row in range(value[0])]
    for train in trains:
        for point in range(train[1] - 1,train[2]):
            matrix[train[0] - 1][point] = 1
        
    count = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == 0:
                count += 1
    return count

def solution2(value, trains):
    point_array = []
    for train in trains:
        for index in range(train[1] - 1, train[2]):
            point_running = [train[0],index]
            if point_running  not in point_array : point_array.append(point_running)
    return (value[0] * value[1] - len(point_array))



value1 = [4,4,3]
test1 = [[2,2,3], [3,1,4], [4,4,4]]

value2 = [4,4,0]
test2 = []

value3 = [0,0,0]
test3 = []

value4 = [5,7,6]
test4 = [[3,1,5], [3,3,7], [5,1,7], [2,2,4], [2,3,5], [2,4,6]]

value5 = [4,4,4]
test5 = [[1,1,4], [2,1,4], [3,1,4], [4,1,4]]

print(solution1(value1,test1))
print(solution1(value2,test2))
print(solution1(value3,test3))
print(solution1(value4,test4))
print(solution1(value5,test5))
print("------------")
print(solution2(value1,test1))
print(solution2(value2,test2))
print(solution2(value3,test3))
print(solution2(value4,test4))
print(solution1(value5,test5))
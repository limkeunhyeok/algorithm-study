def solution(n, m, k, trainPosList):
    visitedSpaceDict = {}
    for trainPos in trainPosList:
        for index in range(trainPos[1] - 1, trainPos[2]):
            visitedSpaceDict[str(trainPos[0]) + ',' + str(index)] = 1

    return n * m - len(visitedSpaceDict.keys())


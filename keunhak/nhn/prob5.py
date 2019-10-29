import sys

MAX_VALUE = 9999999

def solution(n, m, edgeList):
    graph = [{} for _ in range(n + 1)]
    connected = []
    cost = 0

    minWeightedEdge = [-1, -1, MAX_VALUE]

    for edge in edgeList:
        u, v, w = edge
        graph[u][v] = [w, 0] #  w, isConnected
        graph[v][u] = [w, 0]
        if w < minWeightedEdge[2]:
            minWeightedEdge = [u, v, w]

    # initial vertex with minimal weighted edge into connected list
    connected.append(minWeightedEdge[0])
    connected.append(minWeightedEdge[1])
    graph[minWeightedEdge[0]][minWeightedEdge[1]][1] = 1
    graph[minWeightedEdge[1]][minWeightedEdge[0]][1] = 1
    
    cost += minWeightedEdge[2]

    while len(connected) != n:

        # get not connected edge on minimal weight
        minWeightedEdge = [-1, -1, MAX_VALUE]

        for v in connected:
            for u, value in graph[v].items():
                if v in connected and u in connected:
                    continue
                if minWeightedEdge[2] > graph[v][u][0] and graph[v][u][1] == 0:
                    minWeightedEdge = [v, u, graph[v][u][0]]

        # if not exist, return -1
        if minWeightedEdge[0] == -1:
            cost = -1
            break

        # append vertex to connected list
        if minWeightedEdge[0] not in connected: connected.append(minWeightedEdge[0])
        if minWeightedEdge[1] not in connected: connected.append(minWeightedEdge[1])

        cost += minWeightedEdge[2]

        # graph update
        graph[minWeightedEdge[0]][minWeightedEdge[1]][1] = 1
        graph[minWeightedEdge[1]][minWeightedEdge[0]][1] = 1

    return cost

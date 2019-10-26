def solution(N, weights, graph):
    return dfs(weights, graph, '1')

def dfs(weights, graph, startNode):
    path = list()
    visit = list()
    stack = list()

    stack.append(startNode)
    maxWeight = -1
    dest = -1
    
    while stack:
        node = stack.pop()
        path.append(node)
        if node not in visit:
            visit.append(node)
            if node in graph:
                stack.extend(graph[node])
            else:
                weight = maxDist(path, weights)
                if maxWeight < weight:
                    dest = int(path[-1])
                    maxWeight = weight
                elif maxWeight == weight and dest < int(path[-1]):
                    dest = int(path[-1])

                path.pop()

    return str(dest) + " " + str(maxWeight)

def maxDist(path, weights):
    dist = 0
    for station in path:
        dist += weights[int(station) - 1]

    return dist

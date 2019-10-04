import copy

INF = 1000000000

def solution(n, dist):
    visited = [True]
    for i in range(n - 1):
        visited.append(False)

    # 0 부터 시작
    return shortestPath([0], visited, 0, n, dist)

def shortestPath(path, visited, currentLength, n, dist):
    if len(path) == n:
        return currentLength + dist[path[0]][path[-1]]

    ret = INF
    for nextLoc in range(n):
        if visited[nextLoc]: continue

        here = path[-1]
        path.append(nextLoc)
        visited[nextLoc] = True

        cand = shortestPath(copy.deepcopy(path), copy.deepcopy(visited), currentLength + dist[here][nextLoc], n, dist)

        ret = min(ret, cand)
        visited[nextLoc] = False
        path.pop()

    return ret


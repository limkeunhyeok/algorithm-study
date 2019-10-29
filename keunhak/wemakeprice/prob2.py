
def solution(n):
    return withoutZero(n)

def withoutZero(n):
    cnt = 0
    for i in range(1,10):
        target = int(str(i))
        if target == n:
            return cnt
        cnt += 1
        for j in range(1,10):
            target = int(str(i) + str(j))
            if target == n:
                return cnt
            cnt += 1
            for k in range(1,10):
                target = int(str(i) + str(j) + str(k))
                if target == n:
                    return cnt
                cnt += 1
                for t in range(1,10):
                    target = int(str(i) + str(j) + str(k) + str(t))
                    if target == n:
                        return cnt
                    cnt += 1

    return cnt

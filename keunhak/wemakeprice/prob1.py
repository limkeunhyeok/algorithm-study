def solution(n):
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2

    if n % 2 == 1:
        return (solution(int(n/2) + 1) * solution(int(n/2))) + (solution(int(n/2)) * solution(int(n/2) - 1))
    else:
        return (solution(int(n/2)) * solution(int(n/2))) + (solution(int(n/2)-1) * solution(int(n/2)-1))

def solution2(n):
    if n == 1 or n == 0: return 1
    return solution2(n-1) + solution2(n-2)

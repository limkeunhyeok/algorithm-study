'''
def solution(sequence, s):
    if s == 1:
        return calc(sequence)
    else:
        res = 0
        sequence.sort()
        index = diff(sequence, s)
        section = []
        for i in range(s):
            section = sequence[index[i]:index[i+1]]
            res += calc(section)
        return res

def calc(sequence):
    if len(sequence) == 0:
        return 0
    level = round(sum(sequence) / len(sequence))
    res = 0
    for num in sequence:
        res += (num - level)**2
    return res


def diff(sequence, s):
    res = []
    ans = [0]
    for index in range(len(sequence) - 1):
        res.append(sequence[index] - sequence[index + 1])
    temp = 1
    for count in range(s - 1):
       index = res.index(min(res))
       temp += index
       ans.append(temp)
       temp += 1
       res = res[index + 1:]
    ans.append(len(sequence))
    return ans


for T in range(int(input())):
    l, s = map(int, input().strip().split())
    sequence = list(map(int, input().strip().split()))
    if len(set(sequence)) < s:
        s = len(set(sequence))
    print(solution(sequence, s))
'''
def quantize(start, parts):
    if start == n:
        return 0
    if not parts:
        return INF
    ret = cache[start][parts]
    if ret[0] != -1:
        return ret[0]
    ret[0] = INF
    for size in range(1, n - start + 1):
        ret[0] = min(ret[0], min_error(start, start + size - 1) + quantize(start + size, parts - 1))
    return ret[0]


def min_error(start, end):
    psum_begin = 0
    sqsum_begin = 0
    if start:
        psum_begin = partial_sum[start - 1]
        sqsum_begin = partial_sq_sum[start - 1]
    normal_sum = partial_sum[end] - psum_begin
    m = int(0.5 + normal_sum / (end - start + 1))
    ret = (partial_sq_sum[end] - sqsum_begin) - 2 * m * normal_sum + (m ** 2) * (end - start + 1)
    return ret


def pre_calc():
    numbers.sort()
    partial_sum = [numbers[0]] * len(numbers)
    partial_sq_sum = [numbers[0]**2] * len(numbers)
    for i in range(1, len(numbers)):
        partial_sum[i] = partial_sum[i - 1] + numbers[i]
        partial_sq_sum[i] = partial_sq_sum[i - 1] + numbers[i] ** 2
    return partial_sum, partial_sq_sum


INF = 987654321
tc = int(input().strip())
for ti in range(tc):
    n, s = map(int, input().strip().split())
    numbers = [int(x) for x in input().strip().split()]
    cache = [[[-1] for x in range(11)] for y in range(101)]
    partial_sum, partial_sq_sum = pre_calc()
    print(quantize(0, s))
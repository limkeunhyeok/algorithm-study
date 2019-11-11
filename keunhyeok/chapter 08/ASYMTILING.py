# tiling(n) = tiling(n-1) + tiling(n-2)
def tiling(width):
    
    dp = [1,2]
    if width == 1: return 1
    if width == 2: return 2
    for i in range(width- 2):
        dp.append(dp[i] + dp[i+1])
    return dp[-1]

# 전체 타일링 수 - 대칭 타일링 수
def asymmetric(width):
    mod = 1000000007
    if width % 2 == 1:
        res = tiling(width) - tiling(int((width-1)/2))
        return res % mod
    else:
        res = tiling(width) - tiling(int((width + 2)/2))
        return res % mod


for T in range(int(input())):
    width = int(input())
    print(asymmetric(width))
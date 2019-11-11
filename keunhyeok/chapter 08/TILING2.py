def tiling(width):
    mod = 1000000007
    dp = [1,2]
    if width == 1: return 1
    if width == 2: return 2
    for i in range(width- 2):
        dp.append(dp[i] + dp[i+1])
    return dp[-1] % mod

for T in range(int(input())):
    width = int(input())
    print(tiling(width))
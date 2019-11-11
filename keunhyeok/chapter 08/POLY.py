def poly(n):
    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = 1
        for j in range(1, i):
            for k in range(1, i - j + 1):
                dp[i][j] = (dp[i][j] + dp[i - j][k] * (k + j - 1)) % 10000000
    return sum(dp[n]) % 10000000

for T in range(int(input())):
    num = int(input())
    print(poly(num))
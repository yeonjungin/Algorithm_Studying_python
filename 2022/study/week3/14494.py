n, m = map(int, input().split())
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
dp[1][1] = 1

for x in range(1, n + 1):
    for y in range(1, m + 1):
        if x == 1 and y == 1:
            continue
        dp[x][y] = dp[x - 1][y] + dp[x - 1][y - 1] + dp[x][y - 1]

print(dp)
print(dp[n][m] % 1000000007)

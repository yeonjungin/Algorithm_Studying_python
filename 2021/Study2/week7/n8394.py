# n = int(input())
# dp = [0 for _ in range(n + 1)]
# dp[1] = 1
# dp[2] = 2
# for i in range(3, n + 1):
#     dp[i] = dp[i - 1] % 10 + dp[i - 2] % 10
# print(dp[-1] % 10)


x, y = 1, 2
n = int(input())%60
for i in range(1, n):
    x, y = y, (x + y) % 10
print(x)

import sys

n = int(sys.stdin.readline().rstrip())

array = [[0, 0] for _ in range(n)]

for i in range(n):
    array[i] = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0 for _ in range(n + 1)]
term = 0
i = 1

for i in range(n):
    t=array[i][0]
    p=array[i][1]
    if i + t < n+1:
        dp[i + t] = max(dp[i + t], dp[i]+p)
    dp[i + 1] = max(dp[i], dp[i + 1])
print(dp[n])

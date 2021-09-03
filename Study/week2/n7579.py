import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
summy = sum(c)
dp = [0] * (summy + 1)

for i in range(n):
    for j in range(summy, c[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - c[i]] + a[i])

for i in range(summy + 1):
    if dp[i] >= m:
        print(i)
        break

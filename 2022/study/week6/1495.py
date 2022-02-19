n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]  # start, nList
dp[0][s] = True
for i in range(n):
    for j in range(0, m + 1):
        ch = dp[i][j]
        if ch:  # True
            if j + v[i] <= m:
                dp[i + 1][j + v[i]] = True
            if j - v[i] >= 0:
                dp[i + 1][j - v[i]] = True
answer = -1
for i in range(m, -1, -1):
    if dp[n][i]:
        answer = i
        print(answer)
        break
if answer==-1:
    print(-1)

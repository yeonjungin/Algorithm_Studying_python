a, b = input(), input()
lenA = len(a)
lenB = len(b)
dp = [[0 for _ in range(lenB + 1)] for _ in range(lenA + 1)]
answer = 0

for i in range(1, lenA + 1):
    for j in range(1, lenB + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] += dp[i - 1][j - 1] + 1
            answer = max(answer, dp[i][j])
print(answer)

'''
조건 1. 덧셈의 순서가 바뀐 경우 > 다른 경우로 센다.
조건 2. 한 개의 수를 여러번 쓸 수 있다.
출력 : 1000000000으로 나눈 나머지를 출력한다.
'''
n, k = map(int, input().split())
array = [i for i in range(0, n + 1)]
dp = [[0 for _ in range(n)] for _ in range(k)]
dp[0][:] = [1] * n
for i in range(k):
    dp[i][0] = i + 1
    if k==1:
        break
    for j in range(1, n):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j])%1000000000
print(dp[k-1][n-1])
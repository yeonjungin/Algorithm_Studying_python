dp = [1, 1, 1, 2]
t = int(input())
for i in range(t):
    n = int(input())
    if len(dp) < n:
        for _ in range(n - len(dp)):
            dp.append(dp[len(dp) - 3] + dp[len(dp) - 2])
        print(dp[n - 1])
        continue
    # 이미 값이 정해져있는 경우
    print(dp[n - 1])

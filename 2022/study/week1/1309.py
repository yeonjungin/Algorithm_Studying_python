n=int(input())
dp=[1 for _ in range(n+1)]
dp[1]=3

if n==1:
    print(dp[1])
else:
    for i in range(2,n+1):
        #1. i번째 줄에 빈 우리만 있는 경우의 수 : dp[i-1] * 1
        #2. i-1번째 줄에 빈 우리만 있는 경우의 수 : dp[i-2] * 2
        #3. i번째, i-1번째 줄에 모두 배치가 되는 경우의 수 : dp[i-1]-dp[i-2]
        dp[i]=2*dp[i-1]+dp[i-2]
        dp[i]%=9901
    print(dp[n])

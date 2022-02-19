N=int(input())
array=[list(map(int,input().split())) for _ in range(N)]
# 오른쪽이나 아래로만 이동 가능
# 0이 종착점
answer=0

dp=[[0]*N for _ in range(N)]
dp[0][0]=1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:  # 끝에 도달했을 때
            print(dp[i][j])
            break
        cnt = array[i][j]
        # 오른쪽으로 가기
        if j + cnt < N:
            dp[i][j + cnt] += dp[i][j]
        # 아래로 가기
        if i + cnt < N:
            dp[i + cnt][j] += dp[i][j]

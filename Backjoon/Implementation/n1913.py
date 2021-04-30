# https://www.acmicpc.net/problem/1913
n=int(input())
find_num=int(input())
array=[[None]*n for i in range(n)]

# 상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

array[n//2][n//2]=1 # 1 위치 잡아주기
x=n//2 # 현재 x좌표
y=n//2 # 현재 y좌표

for i in range(1,n+1):
    if i%2!=0: #홀수일 경우
        if i==n:
            for _ in range(i-1):
                nx=x+dx[0]
                ny=y+dy[0]
                array[nx][ny]=array[x][y]+1
                x=nx
                y=ny
        else:
            for _ in range(i):
                nx=x+dx[0]
                ny=y+dy[0]
                array[nx][ny]=array[x][y]+1
                x=nx
                y=ny

            for _ in range(i):
                nx = nx + dx[3]
                ny = ny + dy[3]
                array[nx][ny] = array[x][y] + 1
                x=nx
                y=ny

    else: #짝수일경우
        for _ in range(i):
            nx=x+dx[1]
            ny=y+dy[1]
            array[nx][ny]=array[x][y]+1
            x=nx
            y=ny

        for _ in range(i):
            nx=nx+dx[2]
            ny=ny+dy[2]
            array[nx][ny]=array[x][y]+1
            x=nx
            y=ny

        x=nx
        y=ny

for i in range(n):
    for j in range(n):
        print(array[i][j],end=' ')
    print()

for i in range(n):
    for j in range(n):
        if array[i][j]==find_num:
            print(i+1,j+1)
            break
            
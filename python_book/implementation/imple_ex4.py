'''
Chapter4. 구현
실전 3번문제. 게임 개발

'''
n,m=map(int,input().split())
x,y,d=map(int,input().split())
count_map=[[0]*m for _ in range(n)]
count_map[x][y]=1

array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

dx=[0,0,-1,1]
dy=[-1,1,0,0]



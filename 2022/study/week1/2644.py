import sys
sys.setrecursionlimit(300000)
n=int(input())
yeon,kim=map(int,input().split())
m=int(input())
array=[[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]

for _ in range(m):
    p,c=map(int,input().split())
    array[p].append(c)
    array[c].append(p)
    #무방향 그래프니까 둘다 넣어줌

def dfs(node):
    for i in array[node]:
        if not visited[i]:
            visited[i]=visited[node]+1
            dfs(i)
dfs(yeon)
print(visited[kim] if visited[kim]>0 else -1)
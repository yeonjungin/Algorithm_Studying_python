'''
최소 몇 번만에 도착점에 도착할 수 있을까 ? => BFS
'''
from collections import deque

N, M = map(int, input().split())  # N : 사다리, M : 뱀
array = [i for i in range(101)]
visited = [-1 for i in range(101)]
for i in range(N):
    x, y = map(int, input().split())
    array[x] = y
for j in range(M):
    u, v = map(int, input().split())
    array[u] = v


def bfs(node):
    queue=deque() # 큐 생성
    queue.append(node) # 큐에 현재 노드 삽입
    visited[node]=0 # 현재 노드 방문 처리
    while queue:
        idx=queue.popleft()
        for i in range(1,7):
            now=idx+i # now는 현재 idx에 주사위 굴린 수 더한 수
            if now>100:
                continue
            array_num=array[now]
            if visited[array_num]==-1: # 방문하지 않은 곳
                queue.append(array_num)
                visited[array_num]=visited[idx]+1



bfs(1)
print(visited[-1])

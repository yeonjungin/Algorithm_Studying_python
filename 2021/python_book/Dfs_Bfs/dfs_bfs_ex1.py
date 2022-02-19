'''
Chapter5 DFS/BFS
탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
대표적인 탐색 알고리즘 : DFS , BFS

'''

# Ex1 (팩토리얼 : 대표적인 재귀함수 예시)
from collections import deque


def factorial_function(n):
    if n<=1:
        return 1
    return factorial_function(n-1)*n

#Ex2 DFS
'''
1. 시작 노드 방문 처리
2. 시작 노드와 연결되어 있는 노드들을 번호가 낮은 순서대로 탐색을 먼저 시작한다.
3. 만약 현재 노드가 방문처리가 되어있는 노드가 아니라면 더 깊이 탐색 시작(재귀함수 발동!)
'''
def dfs(graph,v,visited): # v는 시작노드
    visited[v]=True #True일 경우, 방문처리한 것
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
graph=[
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8]
    [1,7]
]

visited=[False]*9 # 방문처리 리스트
dfs(graph,1,visited)

# Ex3
'''
1. 큐를 생성한다.
2. 시작 노드를 방문처리한다.
3. 큐가 빌때까지 아래과정을 반복한다.
    3.1 큐의 왼쪽에서 1개를 꺼낸다.
    3.2 방금 꺼낸 노드와 연결되어 있는 다른 노드들중에 방문처리되지 않은 노드가 있으면, 큐에 그 값을 넣고, 해당 노드는 방문처리를한다.
'''
def bfs(graph,start,visited):
    queue=deque([start]) #deque(['a', 'b', 'c', 'd', 'e'])
    visited[start]=True
    while queue: # BFS는 DFS와 다르게 아래 for문이 끝나도 큐에 값이 남아있으니까, 큐가 빌때까지 while문을 또 돌려줘야 함
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

graph=[
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8]
    [1,7]
]

visited=[False]*9 # 방문처리 리스트
dfs(graph,1,visited)









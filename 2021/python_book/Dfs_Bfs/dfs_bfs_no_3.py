'''
Chapter5. DFS/BFS
문제 3번. 음료수 얼려 먹기

1. 구멍이 뚫려있는 부분 0, 칸막이 존재 1
2. 구멍이 뚫려있는 부분끼리 상,하,좌,우 붙어 있는 경우, 서로 연결되어 있다고 간주함

> 이 문제는 사이클이 존재하는 경로를 찾는 경우에 해당
DFS는 한 가지 정점과 연결된 모든 정점을 탐색해야 하는 경우
즉, 경로를 찾아야하는 문제에 활용한다.

'''

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return
    if graph[x][y] == 0:
        graph[x][y] = 1  # 방문처리
        # 상(x-1,y), 좌(x,y-1), 하(x+1,y), 우(x,y+1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)


# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(i, j)
            result += 1

print(result)


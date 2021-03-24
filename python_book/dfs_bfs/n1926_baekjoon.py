'''
백준 1926번
https://www.acmicpc.net/problem/1926

백준 2667번
https://www.acmicpc.net/problem/2667

백준 1012번
https://www.acmicpc.net/problem/1012
'''

n, m = map(int, input().split())  # n : 행, m:열
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

area = 0
max_area = 0

def dfs(x, y):
    global area
    global max_area
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return
    if graph[x][y] == 1:
        graph[x][y] = 0
        area += 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        if max_area < area:
            max_area = area
        area = 0


count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dfs(i, j)
            count += 1

print(count)
print(max_area)

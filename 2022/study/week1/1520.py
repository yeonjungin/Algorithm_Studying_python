import sys
sys.setrecursionlimit(3000000)
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]
# 상,우,하,좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 항상 지금의 높이보다 높이가 더 낮은 지점으로만 이동한다.
# 항상 내리막길로만 이동하는 경로의 수를 구하라
answer = 0


# 맨 오른쪽 좌표 : n-1, m-1
def dfs(x, y):
    global answer
    if x == n - 1 and y == m - 1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            # 맵 안에 있는 경우
            if array[nx][ny] < array[x][y]:
                visited[x][y] += dfs(nx, ny)
    return visited[x][y]


print(dfs(0, 0))

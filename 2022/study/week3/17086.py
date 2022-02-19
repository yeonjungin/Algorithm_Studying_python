# 아기 상어 2
from collections import deque

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

# 상,상우,우,하우,하,하좌,좌,상좌
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

queue = deque()
for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not array[nx][ny]:
                    queue.append((nx, ny))
                    array[nx][ny] = array[x][y] + 1
bfs()
print(max(map(max,array))-1)
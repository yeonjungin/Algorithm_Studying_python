from collections import deque

r, c, k = map(int, input().split())  # 세로,가로,음식물 쓰레기 개수
array = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
for i in range(k):
    n, m = map(int, input().split())
    array[n][m] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

def bfs(i, j):
    global answer
    num = 0
    queue = deque()
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        if array[i][j] == 1:
            num += 1
        array[i][j]=-1
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 < nx <= r and 0 < ny <= c:
                # 맵 안에 있는 경우
                if array[nx][ny] == 1:
                    num += 1
                    array[nx][ny] = -1  # 방문처리
                    queue.append((nx, ny))
                    continue
    answer = max(answer, num)

for i in range(1, r + 1):
    for j in range(1, c + 1):
        if array[i][j] == 1:
            bfs(i, j)

print(answer)

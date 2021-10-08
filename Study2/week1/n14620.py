n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
answer = float('INF')
dx = [1, -1, 0, 0, 0]  # 상,하,좌,우,중앙
dy = [0, 0, -1, 1, 0]


def check(r, c):
    global n
    for i in range(5):
        nx = r + dx[i]
        ny = c + dy[i]
        if visited[nx][ny] or 0 > nx or nx > n - 1 or 0 > ny or ny > n - 1:
            return False
    return True


def dfs(r, cost, cnt):
    global answer
    if cnt == 3:
        answer = min(answer, cost)
        return

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if check(i, j):  # 꽃을 심을 수 있는 환경이다.
                temp = 0
                for k in range(5):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    visited[nx][ny] = 1  # 방문처리
                    temp += array[nx][ny]
                dfs(i, cost + temp, cnt+1)
                for k in range(5):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    visited[nx][ny] = 0  # 방문처리 회수
dfs(1,0,0)
print(answer)
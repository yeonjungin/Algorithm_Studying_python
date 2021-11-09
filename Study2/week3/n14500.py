n, m = map(int, input().split())  # 열 n, 행 m
array = [list(map(int, input().split())) for _ in range(m)]
# 회전 휴리스틱
# 대칭 휴리스틱

'''
5번 반복 ( 테트로미노 가지수가 5개니까)
정방향 최댓값 => 90도 회전 방향 최댓값 -> 180도 회전 방향 최댓값 -> 270도 회전 방향 최댓값 중 max 구해서 넣기
'''
# 우,하,좌,상 (회전)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[0 for _ in range(m)] for _ in range(n)]
answer = 0


def dfs(depth, x, y, value):
    global answer
    if depth == 4:
        answer = max(answer, value)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if visited[nx][ny]:
            continue
        if 0 <= nx < n and 0 <= ny < n:
            # 좌표 내에 있다.
            visited[nx][ny] = 1
            dfs(depth + 1, nx, ny, value + array[nx][ny])
            visited[nx][ny] = 0


for i in range(n):
    for j in range(m):
        dfs(1, i, j, array[i][j])
print(answer)
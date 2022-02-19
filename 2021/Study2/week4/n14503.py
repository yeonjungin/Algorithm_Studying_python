dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
answer = 1
array[r][c] = 2

while True:
    for i in range(4):
        nd = (d + 3) % 4
        nr = r + dx[nd]
        nc = c + dy[nd]

        if array[nr][nc] == 0:
            array[nr][nc] = 2
            answer += 1
            r = nr
            c = nc
            d = nd
            check = 1
            break
        else:
            d-=1
            check = 0

    if i == 3 and check == 0:  # 4방향 다 갈 수 없는 상태인 경우
        nd = (d + 2) % 4
        nr = r + dx[nd]
        nc = c + dy[nd]
        if array[nr][nc] == 1:  # 벽
            break
        else:  # 후진
            r = nr
            c = nc

print(answer)

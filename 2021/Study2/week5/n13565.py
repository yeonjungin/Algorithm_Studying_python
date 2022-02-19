import sys

sys.setrecursionlimit(3000000)
m, n = map(int, input().split())  # m = 행, n = 열
array = [list(map(int, list(input()))) for _ in range(m)]

# 위 = 바깥쪽, 아래 = 안쪽
# 검은색 = 전류차단, 흰색 = 전류 통하는 물질
# 가장 바깥쪽 흰색 격자에 전류 공급
# 상하좌우로 인접한 흰색 격자들로 전달 가능
# array[m-1][] => 값이 채워지면 Yes , 아니면 No
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
button = False


def dfs(row, col):
    global button
    if row == m - 1:  # 안쪽에 닿은 경우
        button = True
        return True

    array[row][col] = 2
    for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        if 0 <= nx < m and 0 <= ny < n and array[nx][ny] == 0:
            dfs(nx, ny)


for k in range(n):
    if array[0][k] == 0:
        dfs(0, k)  # 시작점은 바깥쪽 줄
        if button:
            print("YES")
            break
if not button:
    print("NO")

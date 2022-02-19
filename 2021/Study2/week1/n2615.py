import sys

sys.setrecursionlimit(100000)
array = [[None] for _ in range(19)]

for i in range(19):
    array[i] = list(map(int, input().split()))

# 우상,우,우하,하
dx = [0, 1, 1, -1]
dy = [1, 1, 0, 1]

# 행이 x, 열이 y, 열부터 탐색하는 이유는, 왼쪽, 위쪽이 우선이기 때문이다.
# x와 y의 순서를 바꾸면 오답,,
# x와 y의 순서를 바꾸지 않으려면, 또 다른 작업을 해줘야 한다. > 지나쳤던 부분까지 생각을 해줘야 함..
for x in range(19):
    for y in range(19):
        if array[x][y]:  # 값이 0이 아닐 경우
            color = array[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                cnt = 1

                while 0 <= nx < 19 and 0 <= ny < 19 and array[nx][ny] == color:
                    cnt += 1

                    if cnt == 5:
                        if (0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19) and (
                                array[nx + dx[i]][ny + dy[i]] == color):
                            break

                        if (0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19) and array[x - dx[i]][y - dy[i]] == color:
                            break

                        print(color)
                        print(x + 1, y + 1)
                        sys.exit(0)

                    nx += dx[i]
                    ny += dy[i]
print(0)
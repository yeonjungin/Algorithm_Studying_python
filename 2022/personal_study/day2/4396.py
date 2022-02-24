n = int(input())
# 상, 상우,우,우하,하,하좌,좌,좌상
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
bombArray = [list(input()) for _ in range(n)]
mapArray = [list(input()) for _ in range(n)]
answerArray = [["." for _ in range(n)] for _ in range(n)]
button=False
for i in range(n):
    for j in range(n):
        if mapArray[i][j] == ".":
            continue
        if bombArray[i][j] == ".":
            temp = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if bombArray[nx][ny] == "*":
                        temp += 1
            answerArray[i][j] = str(temp)
        else:
           button=True

if button:
    for i in range(n):
        for j in range(n):
            if bombArray[i][j] == "*":
                answerArray[i][j] = "*"
        print(''.join(answerArray[i]))
else:
    for i in range(n):
        print(''.join(answerArray[i]))

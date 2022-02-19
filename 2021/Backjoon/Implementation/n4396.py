from copy import deepcopy

n = int(input())
map1 = [list(input()) for _ in range(n)]
map2 = [list(input()) for _ in range(n)]
answer = deepcopy(map2)

# 상,우,좌,하
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

temp = False

def boom(array1, array2, answer):
    global temp

    for x in range(n):
        for y in range(n):
            if map2[x][y] == '.':
                continue

            if map2[x][y] == 'x':
                if map1[x][y] == '.':
                    cnt = 0
                    for k in range(8):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx >= 0 and nx < n and ny >= 0 and ny < n:
                            if map1[nx][ny] == '*':
                                cnt += 1
                    answer[x][y] = str(cnt)
                else:
                    temp = True

    if temp:
        return True

    return False


if boom(map1, map2, answer):
    for i in range(n):
        for j in range(n):
            if map1[i][j]=='*':
                answer[i][j]='*'

for i in range(n):
    print(''.join(answer[i]))

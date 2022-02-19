# # 1/11일
# r, c = map(int, input().split())
# array = [list(input()) for _ in range(r)]
# # 늑대 = W, 양 = S
#
# # 상,하,좌,우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# answer = False
#
# for x in range(r):
#     for y in range(c):
#         if array[x][y] == "S":
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if 0 <= nx < r and 0 <= ny < c:
#                     if array[nx][ny] == "W":
#                         print(0)
#                         exit()
#                     elif array[nx][ny] == ".":
#                         array[nx][ny] = 'D'
# print(1)
# for i in range(r):
#     temp = ''
#     for j in range(c):
#         temp += array[i][j]
#     print(temp)

from sys import stdin
input = stdin.readline

def solve():
    r, c = map(int, input().split())
    a = [input().rstrip() for _ in range(r)]
    flag = 1

    for x in range(r):
        if a[x].count('SW') > 0 or a[x].count('WS') > 0:
            flag = 0
            break

    if flag == 0:
        print(0)
        return

    b = [''.join(x) for x in zip(*a)]
    print(b)
    for x in range(c):
        if b[x].count('SW') > 0 or b[x].count('WS') > 0:
            flag = 0
            break

    if flag == 0:
        print(0)
        return
    print(1)

    for x in a:
        print(x.replace('.', 'D'))

if __name__ == '__main__':
    solve()
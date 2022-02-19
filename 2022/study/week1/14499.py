n, m, x, y, k = map(int, input().split())
# 동,서,북,남 = 1,2,3,4
dx = [0,0, 0, -1, 1]
dy = [0,1, -1, 0, 0]
array = [list(map(int, input().split())) for _ in range(n)]
moves = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0, 0]  # 1,2,3,4,5,6(1이 윗면, 6이 바닥면)
top = 0


def moveDice(dir):
    if dir == 1:  # 동쪽
        dice[1], dice[4], dice[3], dice[6] = dice[4], dice[6], dice[1], dice[3]
    elif dir == 2:  # 서쪽
        dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]
    elif dir == 3:  # 북쪽
        dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], dice[1]
    else:  # 남쪽
        dice[1], dice[2], dice[6], dice[5] = dice[2], dice[6], dice[5], dice[1]

def check(nx,ny):
    if array[nx][ny] == 0:
        array[nx][ny] = dice[6]
    else:
        dice[6] = array[nx][ny]
        array[nx][ny]=0
'''
동쪽이동시
4 1 3 6 -> 6 4 1 3

서쪽이동시
4 1 3 6 -> 1 3 6 4

북쪽이동시
2 1 5 6 -> 1 5 6 2 

남쪽이동시
2 1 5 6 -> 6 2 1 5 

'''

for move in moves:
    nx = x + dx[move]
    ny = y + dy[move]
    if 0 <= nx < n and 0 <= ny < m:
        x=nx
        y=ny
        if move == 1:  # 동쪽
            moveDice(move)
            check(nx,ny)
            print(dice[1])
        elif move == 2:  # 서쪽
            moveDice(move)
            check(nx, ny)
            print(dice[1])
        elif move == 3:  # 북쪽
            moveDice(move)
            check(nx, ny)
            print(dice[1])
        else:  # 남쪽
            moveDice(move)
            check(nx,ny)
            print(dice[1])
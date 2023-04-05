# 격자크기 : N * N
# 출처 : https://www.codetree.ai/missions/2/problems/slanted-rectangle/description

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
# 1->2->3->4 방향, 우상, 좌상, 좌하, 우하
dxs = [-1, -1, 1, 1]
dys = [1, -1, -1, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def make_rec(x, y, w, h):  # x,y,가로,세로
    move_list = [w, h, w, h]
    # 출발지 (x,y)
    val = 0
    # 1번 방향
    for dx, dy, move_num in zip(dxs, dys, move_list):
        for _ in range(move_num):
            x, y = x + dx, y + dy
            if not in_range(x, y):
                return 0
            val += array[x][y]
    return val


result = 0
for i in range(n):
    for j in range(n):
        for h in range(1, n):
            for w in range(1, n):
                cur_val = make_rec(i, j, w, h)
                result = max(result, cur_val)

print(result)

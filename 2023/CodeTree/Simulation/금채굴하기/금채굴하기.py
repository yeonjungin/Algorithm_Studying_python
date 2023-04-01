# 채굴한 금의 가격 >= 채굴비용 & 채굴할 수 있는 가장 많은 금의 개수 구하기.
# 격자 크기는 n X n
# 채굴은 마름모 모양으로 딱 1번만 할 수 있다.
# 2차원 영역을 벗어나도 가능함 * (key point)
# 채굴비용 = k*k + (k+1)*(k+1)
# 1개의 금 가격 = m

'''
(풀이)
1. 해당 위치에서 마름모를 했을 때 채굴비용과 채굴할 수 있는 금의 개수를 구하기 (단, k번 이내(=n)로)
'''

n, m = map(int, input().split())  # n:격자크기, m: 금의 가격
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
result = 0


def can_go(x, y):
    return in_range(x, y) and not visited[x][y]


def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


# 채굴비용 <= 금 총액
def total_is_plus(k):
    global m, gcnt
    mining_money = (k * k) + (k + 1) * (k + 1)
    gold_money = gcnt * m
    if mining_money <= gold_money:
        return True
    else:
        return False


def make_rect(x, y, nowk, k):
    global cur_gold_cnt
    if array[x][y] == 1 and can_go(x, y):
        print("plus ", x, ", ", y)
        cur_gold_cnt += 1
    visited[x][y] = True

    if nowk == k:
        return

    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        if can_go(nx, ny):
            make_rect(nx, ny, nowk + 1, k)


# 채굴 비용과 금의 최댓값 개수 구하기
for i in range(n):
    for j in range(n):
        for k in range(n):
            cur_gold_cnt, cur_mining_money = 0, 0
            visited = [[False for _ in range(n)] for _ in range(n)]
            make_rect(i, j, 0, k)
            print("k : ", k, " x : ", i, " y : ", j, "gold_cnt : ", cur_gold_cnt)
        print("--------------")
print(result)


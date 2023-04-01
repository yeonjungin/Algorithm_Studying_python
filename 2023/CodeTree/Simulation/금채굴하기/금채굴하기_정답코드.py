# 채굴한 금의 가격 >= 채굴비용 & 채굴할 수 있는 가장 많은 금의 개수 구하기.
# 격자 크기는 n X n
# 채굴은 마름모 모양으로 딱 1번만 할 수 있다.
# 2차원 영역을 벗어나도 가능함 * (key point)
# 채굴비용 = k*k + (k+1)*(k+1)
# 1개의 금 가격 = m
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
def total_is_plus(k, cur_gold_cnt):
    global m
    mining_money = (k * k) + (k + 1) * (k + 1)
    gold_money = cur_gold_cnt * m
    if mining_money <= gold_money:
        return True
    else:
        return False

def make_rect(x, y, k):
    sum_val=0
    for i in range(n):
        for j in range(n):
            # (x,y)에서 출발해서 인접한 칸으로 최대 k번 이동했을 때 도달 가능한 칸 골라내기
            if abs(x-i)+abs(y-j)<=k:
                sum_val+=array[i][j]
    return sum_val


# 채굴 비용과 금의 최댓값 개수 구하기
for i in range(n):
    for j in range(n):
        for k in range(2*(n-1)+1):
            cur_gold_cnt=make_rect(i, j, k)
            if total_is_plus(k,cur_gold_cnt):
                result=max(result,cur_gold_cnt)

print(result)

'''
n=3일때
k는 최대 4

n=4일때
k는 최대 6
k가 3일때 격자의 반을 채우니까, k가 6이 되면 격자의 모든 칸을 채우게 된다.

n=5일때
k는 최대 8

2*n-2=2*(n-1)

'''

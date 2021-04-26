N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

# 좌, 하, 우, 상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 좌표가 격자 내에 위치해있는지 판단하는 함수.
def inrange(x, y):
    return y < N and y >= 0 and x >= 0 and x < N

# 모래 비율 리스트
array = [
    [0, 0, 2, 0, 0],
    [0, 10, 7, 1, 0],
    [5, 0, 0, 0, 0],
    [0, 10, 7, 1, 0],
    [0, 0, 2, 0, 0]
]

def Turn():
    tmp = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            tmp[i][j] = array[i][j]
    for i in range(5):
        for j in range(5):
            array[4 - j][i] = tmp[i][j]

x = N // 2
y = N // 2
answer = 0  # 날라간 모래의 양
cur = 2
# 이동횟수를 위한 변수이다.
# 2,3,4,5,6,7....을 cur=2로 나누면 1,1,2,2,3,3,...이 나온다.
# 좌 1칸, 하 1칸, 우 2칸, 상 2칸, 좌 3칸, 3칸, 4칸 ,,, 이런식으로 이동이 이루어진다.
dir = 0  # 방향
flag = False

while True:
    cnt = cur // 2  # 이동 횟수 1,1,2,2,3,3,....
    if flag:
        cnt -= 1

    for i in range(0, cnt, 1): #좌,하 / 우,상 한 세트!
        # 좌 step // 우 step
        x += dx[dir]  # y의 좌표x 값
        y += dy[dir]  # y의 좌표y 값
        value = Map[x][y]  # y에 들어있는 값
        # y를 기준으로 해서 (0,0)이라고 가정한다.
        # (-2,-2) ~ (2,2) : 비율 범위
        for j in range(-2, 3, 1):
            for k in range(-2, 3, 1):
                if array[j + 2][k + 2] == 0:  # 값이 0이면 건너뛰기
                    continue
                curx = x + j
                cury = y + k
                curvalue = value * array[j + 2][k + 2] // 100  # 비율 계산한 값
                Map[x][y] -= curvalue  # 처음 주어진 y값에서 방금 계산한 값 빼기
                if inrange(curx, cury) == False:  # False면 격자 밖에 있는 거
                    answer += curvalue
                else:
                    Map[curx][cury] += curvalue # 격자 안에 있으면, 그 자리에 적기
        # 하 step // 상 step
        nx = x + dx[dir]
        ny = y + dy[dir]
        if inrange(nx, ny):
            Map[nx][ny] += Map[x][y]
        else:
            answer += Map[x][y]
        Map[x][y] = 0
    if flag:
        break
    cur+=1
    if cur // 2 == N:
        flag = True
    dir = (dir + 1) % 4
    Turn()

print(answer)

# 코드 출처
# https://github.com/tony9402/baekjoon/tree/main/solution/simulation

# 회전 (이건 비효율적인 코드,,)
# def Turn():
#     tmp = deepcopy(percent_list)
#     ex_tmp = deepcopy(percent_list)
#     array = [0, 0, 0, 0]
#     for k in range(4):
#         if k == 0:
#             array[k] = tmp
#             print(array)
#         else:
#             tmp = deepcopy(array[k - 1])  # deepcopy를 해야 배열의 값이 바뀌지 않는다.
#             for i in range(N):
#                 for j in range(N):
#                     ex_tmp[N - 1 - j][i] = tmp[i][j]
#             array[k] = deepcopy(ex_tmp)
#     return array
#     #좌 0, 하 1, 우 2, 상 3
#
# array=Turn()
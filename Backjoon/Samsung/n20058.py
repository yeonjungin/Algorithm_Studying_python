# 20058번 마법사 상어와 파이어스톰
# https://www.acmicpc.net/problem/20058
'''
import sys
sys.setrecursionlimit(100000) -> 기본 재귀 제한 푸는 법
'''
from collections import deque
from copy import deepcopy

_N, Q = map(int, input().split())
N = pow(2, _N)
map_list = []
map_list = [list(map(int, input().split())) for _ in range(N)]
L_list = list(map(int, input().split()))

ice_map = [list(map(int,input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for l in L_list:
    L = pow(2, l)
    tmp = deepcopy(map_list)
    for x in range(0, N, L):  # 부분격자 행 # 시작,끝,증가폭, 0, 0+k, k<pow(2,N)
        for y in range(0, N, L):  # 부분격자 열
            # k=2**l 간격으로, 행->열순으로 배열을 tmp에 담는 작업
            # 2x2(L=1), 4x4(L=2) 배열로 묶어서 tmp에 저장하는 작업
            # 이제 tmp를 회전시켜서, ice에 넣어서 정보를 수정해줄 예정
            for i in range(L):  # 행
                for j in range(L):  # 열
                    map_list[x + j][L + y - i - 1] = tmp[i + x][j + y]
                    # 과정을 직접 그려볼 것
    tmp = deepcopy(map_list)

    for n in range(N):
        for m in range(N):
            if tmp[n][m] == 0:
                continue
            cnt = 0
            for k in range(4):
                x = n + dx[k]
                y = m + dy[k]
                if y<0 or y>=N or x<0 or x>=N:
                    continue
                if map_list[x][y] != 0:
                    cnt += 1
                    # 상하좌우에 얼음이 0개가 아니라면, cnt+1
            if cnt < 3: # cnt가 3이하면, -1
                tmp[n][m] -= 1
    map_list = deepcopy(tmp)

# 1.남아있는 얼음 A[r][c]의 합
# 2.남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
total = 0
max_ice = 0
L_list=[]
L_list=list(map(int, input().split()))

# 회전하기
for _L in L_list:
    L = pow(2, _L)
    tmp = deepcopy(ice_map)
    for i in range(0, N, L):  # 시작,끝,증가폭, 0, 0+k, k<pow(2,N)
        for j in range(0, N, L):
            # k=2**l 간격으로, 행->열순으로 배열을 tmp에 담는 작업
            # 2x2(L=1), 4x4(L=2) 배열로 묶어서 tmp에 저장하는 작업
            # 이제 tmp를 회전시켜서, ice에 넣어서 정보를 수정해줄 예정
            for n in range(0,L):
                for m in range(0,L):
                    ice_map[i + m][j + L - 1 - n] = tmp[i + n][j + m]
                    # 과정을 직접 그려볼 것

    tmp = deepcopy(ice_map)

    # 인접한 얼음
    for i in range(N):
        for j in range(N):
            if ice_map[i][j] == 0:
                continue
            cnt = 0
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if y < 0 or y >= N or x < 0 or x >= N:
                    continue
                if ice_map[y][x] != 0:
                    cnt += 1
                    # 상하좌우에 얼음이 0개가 아니라면, cnt+1
            if cnt < 3: # cnt가 3이하면, -1
                tmp[i][j] -= 1
    ice_map = deepcopy(tmp)


# 1.남아있는 얼음 A[r][c]의 합
# 2.남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
total=0
max_ice=0

# BFS 알고리즘 (넓이 우선 탐색)
# 단계별 탐색이 가능하기 때문에 최단 거리를 구할 수 있다.
# 최단거리나, 최단 거리를 구하되 조건이 여러 개 존재하는 경우 사용한다.
# 무가중 그래프

for i in range(N):
    for j in range(N):
        if map_list[i][j] == 0:
            continue
        queue = deque()
        queue.append((i, j))
        total += map_list[i][j]
        map_list[i][j] = 0
        cnt = 0
        while len(queue) != 0:
            cx, cy = queue.popleft()  # y가 행, x가 열
            cnt += 1
            for k in range(4):
                x = cx + dx[k]
                y = cy + dy[k]
                if y < 0 or y >= N or x < 0 or x >= N or map_list[x][y] == 0:
                    continue
                queue.append((x, y))
                total += map_list[x][y]
                map_list[x][y] = 0
        max_ice = max(max_ice, cnt)

print("{}\n{}".format(total, max_ice))


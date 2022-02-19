# n20056번 마법사 상어와 파이어볼 문제
# 문제링크 : https://www.acmicpc.net/problem/20056
from copy import deepcopy

N, M, K = map(int, input().split())
M_list = [list(map(int, input().split())) for _ in range(M)]

# M_list[0...4] > r,c,m,s,d #x좌표,y좌표,질량,속력,방향
Map = [[[] for _ in range(N)] for _ in range(N)]  # ***

# 0, 1, 2, 3, 4, ... 순으로
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(M):
    M_list[i][0] -= 1  # x좌표 -1 감소
    M_list[i][1] -= 1  # y좌표 -1 감소
    Map[M_list[i][0]][M_list[i][1]].append([M_list[i][2], M_list[i][3], M_list[i][4]])  # Map리스트에 파이어볼 리스트 담아두기

'''
Map1[0] -> [[0], [0], [0], [0]]
Map1[0][0] -> [0]
Map1[0][0][1] -> 2
'''

for _ in range(K):  # K는 이동횟수
    temp = [[[] for _ in range(N)] for _ in range(N)]  # ***

    # 1. 모든 파이어볼 이동
    for i in range(N):
        for j in range(N):
            if Map[i][j] != []:  # M은 파이어볼 개수
                for x in range(len(Map[i][j])):
                    m, s, d = Map[i][j][x]
                    nx = i + dx[d] * s
                    ny = j + dy[d] * s
                    nx = (nx + N) % N
                    ny = (ny + N) % N
                    temp[nx][ny].append([m, s, d])
    # 2. 2개 이상의 파이어들이 있는 칸을 찾아가서 4개의 파이어들로 다시 만드는 과정
    for x in range(N):
        for y in range(N):
            if len(temp[x][y]) > 1:
                list_cnt = len(temp[x][y])
                n_m, n_s, d = 0, 0, []
                for z in range(list_cnt):
                    n_m += temp[x][y][z][0]
                    n_s += temp[x][y][z][1]
                    d.append(temp[x][y][z][2] % 2)
                n_m = int(n_m // 5)
                n_s = int(n_s / list_cnt)
                temp[x][y] = []
                if n_m != 0:
                    if sum(d) == 0 or sum(d) == list_cnt:  # 모두 홀수이거나 또는 짝수인 경우
                        for i in range(4):
                            temp[x][y].append([n_m, n_s, i * 2])
                    else:
                        for i in range(4):
                            temp[x][y].append([n_m, n_s, i * 2 + 1])
    Map = deepcopy(temp)

answer = 0
for i in range(N):
    for j in range(N):
        if Map[i][j]:  # 내용물이 있을 경우를 찾는다.
            len_num = len(Map[i][j])
            for n in range(len_num):
                answer += Map[i][j][n][0]
print(answer)

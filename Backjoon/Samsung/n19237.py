# N : 격자크기, M : 상어가 들어있는 칸의 개수, K : 냄새 지속시간
N, M, K = map(int, input().split())

# 격자 (Map은 2차원 배열)
Map = [list(map(int, input().split())) for _ in range(N)]
'''
Map = []
for i in range(N):
    Map.append(list(map(int, input().split())))
'''

# 현재 상어들의 방향 #1,2,3,4번 상어 순
directions = list(map(int, input().split()))

# 상어들의 우선순위
shark_priority = [[] for _ in range(M)]
for i in range(M):
    for j in range(4):
        shark_priority[i].append(list(map(int, input().split())))
'''
Shark_priority = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]
'''

# 냄새는 또 다른 리스트에 담기, 크기는 Map 크기와 동일
# 냄새리스트[상어 번호, 냄새 지속타임]
# for는 [] 자체를 복사, * N 은 내용만 복사
smell = [[[0, 0] for _ in range(N)] for _ in range(N)]
'''
smell=[[[0,0]] * N for _ in range(N)]
'''

# 상, 하 , 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time = 0

while True:
    # 모든 상어가 자신의 위치에 냄새를 뿌린다.
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] > 0: # 만약 현재 위치에 냄새가 있다면?
                smell[i][j][1] -= 1 # 냄새 지속 시간 -1
            if Map[i][j] != 0: # 현재 위치에 냄새 뿌리기
                smell[i][j] = [Map[i][j], K]

    # 그 후에 1초마다 모든 상어가 이동하고 자신의 냄새를 그 칸에 뿌린다.

    temp = [[0 for _ in range(N)] for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if Map[x][y]:
                now_dir = directions[Map[x][y] - 1] # 현재 모든 상어의 방향
                we_found = False
                # 인접한 칸 중에 아무 냄새가 없는 칸을 찾는다.
                for z in range(4):
                    # -1은 문제에서 1부터 시작했기 때문에 인덱스 맞추려고 하는 과정
                    nx = x + dx[shark_priority[Map[x][y] - 1][now_dir - 1][z] - 1]
                    ny = y + dy[shark_priority[Map[x][y] - 1][now_dir - 1][z] - 1]
                    # dx[우선순위리스트[현재 상어번호][현재 상어가 바라보는 방향][idx]-1]
                    if nx >= 0 and nx < N and ny >= 0 and ny < N:
                        if smell[nx][ny][1] == 0:  # 아무 냄새가 없을 경우
                            directions[Map[x][y] - 1] = shark_priority[Map[x][y] - 1][now_dir - 1][z]
                            if temp[nx][ny] == 0:
                                temp[nx][ny] = Map[x][y]
                            else:
                                temp[nx][ny] = min(temp[nx][ny], Map[x][y])
                            we_found = True
                            break

                # 위에서 칸을 찾았는지 안 찾았는지 체크하는 단계
                if we_found:
                    continue

                # 모든 칸에 냄새가 차 있어서 위에서 움직이지 못했을 경우, 이제 자신의 냄새가 있는 칸을 찾는다.
                for index in range(4):
                    nx = x + dx[shark_priority[Map[x][y] - 1][now_dir - 1][index] - 1]
                    ny = y + dy[shark_priority[Map[x][y] - 1][now_dir - 1][index] - 1]
                    if nx >= 0 and nx < N and ny >= 0 and ny < N: # 격자 내에 존재할 때
                        if smell[nx][ny][0] == Map[x][y]:
                            directions[Map[x][y] - 1] = shark_priority[Map[x][y] - 1][now_dir - 1][index]
                            temp[nx][ny] = Map[x][y]
                            break

    Map = temp
    time += 1

    #1번 상어만 남았는지 체크하기
    check = True
    for i in range(N):
        for j in range(N):
            if Map[i][j] > 1:
                check = False

    if check:
        print(time)
        break

    if time >= 1000:
        print(-1)
        break
'''
# 순서 (큰틀)
1. 모든 상어가 자신의 위치에 냄새를 뿌린다.
2. 그 후에 1초마다 모든 상어가 이동하고 자신의 냄새를 그 칸에 뿌린다.
(냄새는 상어가 K번 이동하면 사라진다.)

# 제약 (상어 이동방향)
우선순위가 있음!
1. 아무냄새가 없는 칸 ( 순서는 정해진 우선순위에 따라서 변동 ) 
2. 모든 칸에 냄새가 차있으면, 자신의 냄새가 있는 칸을 선택
(만약 가능한 칸이 여러개이면, 그땐 정해진 우선순위에 따라 변동된다)

'''

# 참고 출처
# https://github.com/ndb796/python-for-coding-test/blob/master/19/3.py

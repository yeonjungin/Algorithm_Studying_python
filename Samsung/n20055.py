import sys
from collections import deque

# https://chaewonkong.github.io/posts/python-deque.html
# 코드 출처 : https://jainn.tistory.com/81

input = sys.stdin.readline

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * N)
cnt = 0

while True:
    # 1단계 : 벨트 회전
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0  # 로봇이 내려가는 부분
    # print("1단계 robot", robot)
    # print("1단계 belt", belt)
    # 2단계
    if sum(robot):  # 로봇이 존재하는 경우
        for i in range(N - 2, -1, -1):  # 가장 먼저 벨트가 올라간 로봇부터 회전하는 방향으로 이동이 가능해야 함
            if robot[i + 1] == 0 and belt[i + 1] >= 1 and robot[
                i] == 1:  # 현재 칸에 로봇이 있고, 다음 칸에 로봇이 없는 상티염, 다음 칸의 내구도가 1이상 남아 있는 경우에만 이동이 가능
                robot[i + 1] = 1
                belt[i + 1] -= 1
                robot[i] = 0
        robot[-1] = 0
        # print("2단계 robot", robot)
        # print("2단계 belt", belt)

    # 3단계
    if robot[0] == 0 and belt[0]>=1:
        robot[0] = 1
        belt[0] -= 1
    # print("3단계 robot", robot)
    # print("3단계 belt", belt)
    cnt += 1 # 계산 횟수 구하는 단계

    # 4단계
    if belt.count(0) >= K:
        break
    # print("4단계 robot", robot)
    # print("4단계 belt", belt)
    # print("============================")

print(cnt)

'''
   for i in range(N):
    if belt[i]==0:
        cnt+=1
if cnt>=K:
    break
'''

# print(belt)
# print(robot)
# robot=deque([0] * N)
# print(robot)
# robot=deque([i] for i in range(N))
# print(robot)


# i=0 [1],[2]..[N], i=1 [N+1], [N+2] ..[2N]

# 회전, 우,좌
# dx = [0,0]
# dy = [1,-1]
#
# robot = 99
#
# temp = deepcopy(Map)
# # 벨트 회전
# x = 0
# y = 0

# for i in range(2):
#     for j in range(N):
#         nx = i+dx[i]
#         ny = j+dy[i]
#         nx = (nx + N) % N
#         ny = (ny + N) % N
#         print(nx,ny)

# while True:
#     cnt = 0
#     for i in range(len(A_list)):
#         if A_list[i] == 0:
#             cnt += 1
#     if cnt >= K:
#         break
#     else:
#         x = 0
#         y = 0

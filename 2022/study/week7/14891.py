'''
맞닿은 극이 다르다면 B는 A가 회전한 방향과 반대 항뱡으로 회전
극이 같으면 회전하지 않음
'''
from collections import deque

gear = [deque(map(int, input())) for _ in range(4)]
# N극 : 0 , S극 : 1
# 12시 방향부터 시게 방향으로 주어짐 (오른쪽 방향)
k = int(input())
array = [deque(list(map(int, input().split()))) for _ in range(k)]


def left(num, dir):
    if num < 0:
        return
    if gear[num + 1][6] != gear[num][2]:
        left(num-1,-dir)
        gear[num].rotate(dir)


def right(num, dir):
    if num > 3:
        return
    if gear[num - 1][2] != gear[num][6]:
        right(num+1,-dir)
        gear[num].rotate(dir)


for i in range(k):
    rnum, rdir = array[i]
    rnum -= 1
    left(rnum - 1, -rdir)  # 왼쪽 톱니바퀴 변경
    right(rnum + 1, -rdir)  # 오른쪽 톱니바퀴 변경
    gear[rnum].rotate(rdir)

answer = 0
if gear[0][0] == 1:  # s극
    answer += 1
if gear[1][0] == 1:
    answer += 2
if gear[2][0] == 1:
    answer += 4
if gear[3][0] == 1:
    answer += 8
print(answer)

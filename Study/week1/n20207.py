# 20207. 달력'
'''
구현 문제
> 처음엔 2차원 배열에 시작점과 끝점을 다 넣어줘야하나 고민했다.
> 하지만 그렇게 되면, 연속지점은 어찌저찌 구하더라도 중간에 끊어지는 부분이나, 코팅지 면적의 높이를 구할 수 없게 된다.
> 이 문제는 일단 365개의 숫자가 들어갈 배열을 구해야한다.
> 1일부터~ 365일까지니까, 크기가 366인 배열을 만들어서 0번째 배열은 버리고 1번째 배열부터 사용할 예정이다.
> calendar 배열에는 row(높이)의 정보만을 담을 것이다.
>


'''
import sys

n = int(input())
calendar = [0 for _ in range(367)]  # 달력 초기화
# 배열의 크기가 367인 이유는?
# > 만약 calendar[365]가 1일경우, answer+=row*col이 실행되지 않기때문에,
# > 배열 크기는 366+1 = 367로!
# > calendar[366]이 0이면, answer+=row*col 실행된다.

# 배열 원소에는 row 값 넣을 예정
for _ in range(n):
    start, end = map(int, input().split())
    for i in range(start, end + 1):
        calendar[i] += 1

row = 0  # 높이
col = 0  # 너비
answer = 0

# row의 최대값과 연속된 칸의 개수를 곱하면 -> 코팅지 면적이 나온다.
for i in range(1, 367):
    if calendar[i] != 0:  # 현재 칸이 채워져있음
        row = max(row, calendar[i])
        col += 1
    else:  # 현재 칸이 0이라면?
        answer += row * col
        row, col = 0, 0


print(answer)

# 20436. ZOAC 3
# 자음=왼쪽(5,5,4), 모음=오른쪽(6~10,6~9,5~7)
# 거리 |x1-x2|+|y1-y2|
# 최솟값 구하기
keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm']]

sl, sr = input().split()


def find_current_location(s):
    for i, key in enumerate(keyboard):
        if s in key:
            return i, key.index(s)
    return None


slx, sly = find_current_location(sl)  # 왼손 현위치
srx, sry = find_current_location(sr)  # 오른손 현위치
answer = 0

for i in input():
    x, y = find_current_location(i)
    if ((x == 0 or x == 1) and y < 5) or (x == 2 and y < 4):  # 자음
        # 이동
        answer += abs(slx - x) + abs(sly - y)
        slx = x
        sly = y
        # 누르기
        answer += 1
    else:  # 모음
        # 이동
        answer += abs(srx - x) + abs(sry - y)
        srx = x
        sry = y
        # 누르기
        answer += 1

print(answer, end='')
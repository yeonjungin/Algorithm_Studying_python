'''
A~H : 열
8
7
...
1 : 행
'''

# T,RT,R,RB,B,LB,L,LT
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
dic = {'T': 0, 'RT': 1, 'R': 2, 'RB': 3, 'B': 4, 'LB': 5, 'L': 6, 'LT': 7}

king, dol, n = input().split()
king = list(king)  # 열, 행
dol = list(dol)  # 열, 행
n = int(n)

for _ in range(n):
    move = input()
    move_num = dic.get(move)  # 이동 idx
    knx = int(king[1]) - dx[move_num]  # 킹 행
    kny = ord(king[0]) + dy[move_num]  # 킹 열
    dnx = int(dol[1]) - dx[move_num]  # 돌 행
    dny = ord(dol[0]) + dy[move_num]  # 돌 열

    if 0 < knx < 9 and 64 < kny < 73:  # 격자 안에 있으면
        if chr(kny) == dol[0] and knx == int(dol[1]):  # 도착 위치에 돌이 있을 경우 -> 같은 방향으로 한칸 이동 (킹방향)
            if 0 < dnx < 9 and 64 < dny < 73:  # 돌도 격자 안에 있을 경우
                dol = [chr(dny), str(dnx)]
                king = [chr(kny), str(knx)]
                continue
            continue
        king = [chr(kny), str(knx)]


k_result = ''
for i in king:
    k_result += i
d_result = ''
for i in dol:
    d_result += i
print(k_result)
print(d_result)

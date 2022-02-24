sL, sR = input().split()
inp_str = list(input())

left_keybord = {'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4), 'a': (1, 0), 's': (1, 1), 'd': (1, 2),
                'f': (1, 3), 'g': (1, 4), 'z': (2, 0), 'x': (2, 1), 'c': (2, 2), 'v': (2, 3)}
right_keybord = {'y': (0, 5), 'u': (0, 6), 'i': (0, 7), 'o': (0, 8), 'p': (0, 9), 'h': (1, 5), 'j': (1, 6), 'k': (1, 7),
                 'l': (1, 8), 'b': (2, 4), 'n': (2, 5), 'm': (2, 6)}

lx, ly = left_keybord[sL]
rx, ry = right_keybord[sR]

answer = 0
cnt=0
for str in inp_str:
    if str in left_keybord:  # 왼쪽
        nx, ny = left_keybord[str][0], left_keybord[str][1]
        answer += abs(nx - lx) + abs(ny - ly)
        lx, ly = nx, ny
        cnt+=1
        continue
    else:  # 오른쪽
        nx, ny = right_keybord[str][0], right_keybord[str][1]
        answer += abs(nx - rx) + abs(ny - ry)
        rx, ry = nx, ny
        cnt+=1
print(answer+cnt)

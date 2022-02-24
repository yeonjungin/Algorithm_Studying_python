num = int(input())
num -= 1
x, y = (4 * num + 1) // 2, (4 * num + 1) // 2
array = [[' ' for _ in range(4 * num + 1)] for _ in range(4 * num + 1)]
array[x][y] = "*"
idx = 0
for _ in range((num + 1) * 2 - 1):
    if idx == 0:
        idx += 1
        continue
    if idx % 2 == 0:
        for i in range(2*idx+1):
            array[x - idx][y - idx + i] = "*"  # 윗줄
            array[x - idx + i][y - idx] = "*"  # 왼쪽 세로줄
            array[x - idx + i][y + idx] = "*"  # 오른쪽 세로줄
            array[x + idx][y - idx + i] = "*"  # 아랫줄
    idx += 1
for i in range((4*num)+1):
    print(''.join(array[i]))

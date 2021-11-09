k = int(input())
array = [list(map(int, input().split())) for _ in range(6)]

longW = 0
longH = 0
longWidx = 0
longHidx = 0

shortW = 0
shortH = 0

# 왼쪽 : 2, 오른쪽: 1, 위 : 4, 아래 : 3
# longW => 왼쪽, 오른쪽 탐색
# longH => 위, 아래 탐색

for idx, temp in enumerate(array):
    if temp[0] == 1 or temp[0] == 2:
        if longW < temp[1]:
            longWidx = idx
            longW = temp[1]

    elif temp[0] == 3 or temp[0] == 4:
        if longH < temp[1]:
            longHidx = idx
            longH = temp[1]

shortW = abs(array[(longWidx - 1) % 6][1] - array[(longWidx + 1) % 6][1])
shortH = abs(array[(longHidx - 1) % 6][1] - array[(longHidx + 1) % 6][1])
print(abs(((longW * longH) - (shortW * shortH)))* k)

h, w = map(int, input().split())  # 세로,가로
array = list(map(int, input().split()))
cnt = 0

for i in range(0, len(array)):
    left = max(array[:i + 1])
    right = max(array[i:])

    if array[i]>min(left,right):
        continue
    else:
        cnt+=min(left,right)-array[i]

print(cnt)

'''
h, w = map(int, input().split())  # 세로,가로
array = [[0 for _ in range(w)] for i in range(h)]
b_h = list(map(int, input().split()))
for i in range(w):
    if b_h[i] == 0:
        continue
    for j in range(b_h[i]):
        array[h - 1 - j][i] = 1

answer = 0

for i in range(h - 1, -1, -1):
    start = 0
    end = 0
    num = 0

    for j in range(w):
        if start == 0:
            if array[i][j] == 1:
                start = 1
                continue
        else:
            if end == 0:
                if array[i][j] == 0:
                    if j == w - 1:
                        continue
                    num += 1
                    continue
                else:
                    end = 1
                    answer += num
                    num = 0
                    continue
            else:
                if array[i][j] == 1:
                    continue
                else:
                    end = 0
                    num += 1
    if start == 1 and end == 0:
        num = 0
    else:
        answer += num
print(answer)
'''

n, m = map(int, input().split())
array = [input() for _ in range(n)]
row = 0
col = 0

for i in range(n):
    if "X" not in array[i]:
        row += 1

for i in range(m):
    cnt = 0
    for k in range(n):
        if "X" not in array[k][i]:
            cnt += 1
    if cnt == n:
        col += 1
print(max(row, col))

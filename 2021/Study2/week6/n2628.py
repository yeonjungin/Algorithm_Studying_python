col, row = map(int, input().split())
rows = [0, row]  # 행
cols = [0, col]  # 열

for _ in range(int(input())):
    now, num = map(int, input().split())
    if now:  # 세로
        cols.append(num)
    else:
        rows.append(num)

rows.sort()
cols.sort()
answer = 0

for i in range(len(rows) - 1):
    for j in range(len(cols) - 1):
        answer = max(answer, (cols[j + 1] - cols[j]) * (rows[i + 1] - rows[i]))

print(answer)

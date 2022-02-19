n, m = map(int, input().split())
array = [list(map(int, input())) for _ in range(n)]
# 가장 큰 정사각형의 넓이
answer = 0

for i in range(1, n):
    for j in range(1, m):
        if array[i][j]:
            array[i][j] += min(array[i-1][j-1],array[i-1][j],array[i][j-1])

for row in array:
    answer = max(answer, max(row))
print(answer ** 2)

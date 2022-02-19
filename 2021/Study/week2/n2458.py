import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
array = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    array[a - 1][b - 1] = 1

# i->k->j : i와 j가 연결되어 있는지 확인하는 과정
# k는 경유지, i는 출발지, j는 도착지
for k in range(n):
    for i in range(n):
        for j in range(n):
            if array[i][k] == 1 and array[k][j] == 1:
                array[i][j] = 1

print(array)

answer = 0
for i in range(n):
    check = 0
    for j in range(n):
        check += array[i][j] + array[j][i]
    if check == n - 1:
        answer += 1
print(answer)

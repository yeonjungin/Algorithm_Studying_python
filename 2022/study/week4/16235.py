import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
aArray = [list(map(int, input().split())) for _ in range(n)]
locationArray = [[[] for _ in range(n)] for _ in range(n)]

for i in range(m):
    x, y, z = map(int, input().split())
    locationArray[x - 1][y - 1].append(z)
nowFoodArray=[[5] * n for _ in range(n)]
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]
answer = 0


for year in range(k):
    for i in range(n):
        for j in range(n):
            if locationArray[i][j]:
                locationArray[i][j].sort()
                temp = []
                died=0
                for age in locationArray[i][j]:
                    if age <= nowFoodArray[i][j]:
                        nowFoodArray[i][j] -= age
                        age += 1
                        temp.append(age)
                    else:
                        died += age // 2
                nowFoodArray[i][j]+=died
                locationArray[i][j] = []
                locationArray[i][j].extend(temp)
    if not locationArray:
        print(0)
        sys.exit()
    for i in range(n):
        for j in range(n):
            if locationArray[i][j]:
                for age in locationArray[i][j]:
                    if age % 5 == 0:
                        for d in range(8):
                            nx = i + dx[d]
                            ny = j + dy[d]
                            if 0 <= nx < n and 0 <= ny < n:
                                locationArray[nx][ny].append(1)
    for i in range(n):
        for j in range(n):
            nowFoodArray[i][j] += aArray[i][j]

for i in range(n):
    for j in range(n):
        answer += len(locationArray[i][j])
print(answer)


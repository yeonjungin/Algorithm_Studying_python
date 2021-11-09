'''
빈칸 0 ,집 1, 치킨집 2
(1,1)~

도시의 치킨 거리 = 모든 집의 치킨 거리

'''
from itertools import combinations

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            houses.append((i, j))
        elif array[i][j] == 2:
            chickens.append((i, j))

answer = 1000000000
for chicken in combinations(chickens, m):  # chicken에서 최대 m개의 치킨집을 고르는 수
    sum = 0
    for house in houses:
        sum += min([abs(house[0] - i[0]) + abs(house[1] - i[1]) for i in chicken])
    if answer > sum:
        answer = min(answer, sum)

print(answer)

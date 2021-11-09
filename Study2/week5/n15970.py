n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

# 조합, 정렬, min(거리)
array = sorted(array, key=lambda x: x[1])
answer = 0
for i in range(len(array)):
    answer += min([abs(array[x][0] - array[i][0]) for x in range(n) if x != i and array[x][1] == array[i][1]])
print(answer)

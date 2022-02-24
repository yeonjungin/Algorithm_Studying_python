n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
cows = [-1 for _ in range(11)] # *****

answer = 0
for arr in array:
    num, location = arr[0], arr[1]
    if cows[num] == -1:
        cows[num] = location
        continue
    if cows[num] != location:
        answer += 1
        cows[num]=location
print(answer)

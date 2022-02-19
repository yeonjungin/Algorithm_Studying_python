f, e = map(int, input().split())
temp = 1
answer = []

while len(answer) < e:
    for _ in range(temp):
        answer.append(temp)
    temp += 1
print(sum(answer[f-1:e]))

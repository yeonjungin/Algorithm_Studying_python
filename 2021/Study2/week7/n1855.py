k = int(input())  # 열
temp = input()
num = len(temp) // k  # 행
array = [[] for _ in range(k)]

for i in range(1, num + 1):
    if i%2==1:
        for j in range(k):
            array[j].append(temp[j])
        temp=temp[k:]
    else:
        for j in range(k):
            array[j].append(temp[k-j-1])
        temp=temp[k:]

answer=''
for arr in array:
    for i in arr:
        answer+=i
print(answer)
'''
    if i % 2 == 1:  # 홀수 왼쪽->오른쪽
        for j in range(cnt, len(temp), 4):
            answer += temp[j]
            cnt = j
        cnt += 1
    else:  # 오른쪽 <- 왼쪽
        for j in range(cnt, 0, -4):
            answer += temp[j]
            cnt = j
        cnt += 1
'''

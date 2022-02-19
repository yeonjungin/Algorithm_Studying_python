t = int(input())
nums = [int(input()) for _ in range(t)]
temp = [1 for _ in range(100001)]
prime = []

for i in range(2, 100001):
    if temp[i]:
        prime.append(i)
        for j in range(i * 2, 100001, i):
            if j > 100000:
                break
            temp[j] = 0

for num in nums:
    answer = []
    for i in prime:
        if i > num:
            break
        if num % i == 0:
            cnt = 0
            while num % i == 0:
                cnt += 1
                num = num // i
            answer.append([i, cnt])
    for a, b in answer:
        print(a, b)

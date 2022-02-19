t = int(input())
MAX = 1000000
array = [1 for _ in range(MAX + 1)]
prime = []

# 소수 집합 구하기
for i in range(2, MAX + 1):
    # 에라토스테네체 = 소수!!!
    if array[i]:
        prime.append(i)
        for j in range(i * 2, MAX + 1, i):
            # 배수 지우는 작업
            if j > MAX:
                break
            array[j] = 0

for _ in range(t):
    n = int(input())
    answer = 0
    for i in prime:
        if n - i < i:
            break
        if array[n - i]:
            answer += 1
    print(answer)

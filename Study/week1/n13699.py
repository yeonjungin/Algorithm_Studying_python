# 점화식. 13699번
# 알고리즘 분류 : 다이나믹 프로그래밍, 메모이제이션
n = int(input())
array = [0 for _ in range(n + 1)]
array[0] = 1

for i in range(1, n + 1):
    for j in range(0, i, 1):
        array[i] += array[j] * array[i - j - 1]

print(array[n])

'''
array[1],array[2],array[3] .. 순차적으로 값을 구해서 array에 집어넣어야함.
이중 반복문 사용

'''
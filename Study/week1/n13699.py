# 점화식. 13699번
# 알고리즘 분류 : 다이나믹 프로그래밍, 메모이제이션
n = int(input())
array = [0 for _ in range(n + 1)]
array[0] = 1

for i in range(1, n + 1):
    for j in range(i):
        array[i] += array[j] * array[i - j - 1]

print(array[n])

'''
i=1
array[1]=array[0]*array[0]

i=2
array[2]=array[0]*array[1]+array[1]*array[0]

i=3
array[3]=array[0]*array[2]+array[1]*array[1]+array[2]*array[0]


array[i]=array[j]*array[i-j-1]
'''
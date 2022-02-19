'''
산성 - 양의 정수
알칼리성 - 음의 정수
'''
import sys

n = int(input())
array = sorted(list(map(int, input().split())))
answer = []
temp = sys.maxsize
for i in range(n - 2):
    left = i + 1
    right = n - 1
    while left < right:
        sumValue = array[i] + array[left] + array[right]
        if abs(sumValue) < temp:
            answer = [array[i], array[left], array[right]]
            temp = abs(sumValue)
        if sumValue < 0:
            left += 1
        elif sumValue > 0:
            right -= 1
        else:
            break

print(*answer)

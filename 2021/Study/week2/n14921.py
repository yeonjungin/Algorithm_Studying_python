import sys

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))

left = 0
right = n - 1

result = 100000000

while left < right:
    now = array[left] + array[right]
    if now == 0:
        print(0)
        break

    if now > 0:
        right -= 1
        if abs(result)>abs(now):
            result=now
            continue
        continue

    left += 1
    if abs(result)>abs(now):
        result=now

print(result)
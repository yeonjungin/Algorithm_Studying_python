import sys
input = sys.stdin.readline

n, m = map(int, input().split())
T = [int(input().rstrip()) for _ in range(n)]
left = 0
right = min(T) * m
result = right

if n == 1:
    result = T[0] * m
    print(result)
else:
    while left < right:
        mid = (left + right) // 2
        cnt = 0
        for t in T:
            cnt += mid // t

        if cnt < m:
            left = mid + 1
        else:
            result = min(mid, result)
            right=mid
    print(result)

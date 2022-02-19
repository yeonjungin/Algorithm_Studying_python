# 01타일
'''
n=4
1111 : 1이 4개
1110 x : 1이 3개 , 0이 1개, 0이 1개면 안된다.
1100 o : 1이 2개, 0이 2개
1000 x : 1이 1개, 0이 3개
0000 o : 1이 0개, 0이 4개

1의 개수 n, n-2, n-4

n=3
111 : 1 3개
100 : 1 1개
000 : 1 0개


'''
# n=int(input())
# dp=[0] * 1000001
#
# dp[1]=1
# dp[2]=2
#
# for i in range(3,n+1):
#     dp[i]=(dp[i-1]+dp[i-2])%15746
# print(dp[n])

n=int(input())

def mul(a, k):
    if k == 1:
        b = A
    elif k == 2:
        b = a
    else:
        b = B
    return (
        (a[0] * b[0] + a[1] * b[2]) % 15746,
        (a[0] * b[1] + a[1] * b[3]) % 15746,
        (a[2] * b[0] + a[3] * b[2]) % 15746,
        (a[2] * b[1] + a[3] * b[3]) % 15746
    )


A, B = (1, 1, 1, 0), (1, 0, 0, 1)
'''
행렬 A, B
[1 1]   [1 0]
[1 0]   [0 1]
A에 B를 곱해도 항상 값은 A
'''

def solve(n):
    if n == 1:
        return mul(A, 0)
    if n % 2 == 1:
        return mul(solve(n - 1), 1)
    return mul(solve(n // 2), 2)  # n이 2의 제곱일 경우, n=16이면, solve(8),k=2, [행렬]^8 * [행렬]^2


print(solve(n))

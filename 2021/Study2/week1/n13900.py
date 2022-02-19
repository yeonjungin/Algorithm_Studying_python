'''
4
1 2 3 4
2 + 3 + 4 + 6 + 8 + 12 = 44

'''
# from itertools import permutations, combinations
#
# num = int(input())
# inp = list(map(int, input().split()))
# for i in inp:
#     arr=list(combinations(i,2))
# arrs = list(combinations(inp, 2))
# result = 0
#
# for arr in arrs:
#     x, y = arr
#     result += x * y
#
# print(result)
# -> 메모리초과

# -> 시간초과
# import sys
#
# num = int(sys.stdin.readline())
# inp = list(map(int, sys.stdin.readline().rstrip().split()))
# result = 0
#
# for i in range(num - 1):
#     for j in range(i + 1, num):
#         result += inp[i] * inp[j]
# print(result)

import sys

num = int(sys.stdin.readline())
inp = list(map(int, sys.stdin.readline().rstrip().split()))
result = 0
subsum = sum(inp)

for i in inp:
    subsum-=i
    result+=subsum*i



print(result)
'''
4
1 2 3 4
1*(2+3+4)
2*(3+4)
3*(4)

i=1, 2, 3, 4
result= 0,2,9,24
subsum=1,3,6,10
2 + 9 + 24 = 35
    
(1*2) + (1*3) + (1*4)
(2*3) + (2*4) 
(3*4)
'''

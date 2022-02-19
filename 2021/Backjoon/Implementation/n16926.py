# 16926번 배열 돌리기 1
n, m, r = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]


def rotate():
    global array
    cut_line = min(n, m) // 2


    for _ in range(r):
        fr, br = 0, n - 1  # 기준점 좌표
        fc, bc = 0, m - 1
        while cut_line and fr < cut_line:
            key = array[fr][fc]

            fr_br = br - fr  # 행
            fc_bc = bc - fc  # 열

            # 1번, 좌
            array[fr][fc:bc] = array[fr][fc + 1:bc + 1]

            # 2번, 상

            cnt = 0
            for _ in range(fr_br):
                array[fr + cnt][bc] = array[fr + cnt + 1][bc]
                cnt += 1

            # 3번, 우
            array[br][fc + 1:bc + 1] = array[br][fc:bc]

            # 4번, 하
            cnt = 0
            for _ in range(fr_br):
                array[br - cnt][fc] = array[br - cnt - 1][fc]
                cnt += 1

            array[fr + 1][fc] = key

            fr += 1
            br -= 1
            fc += 1
            bc -= 1


rotate()
for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print()


# import sys
# from copy import deepcopy
#
#
# def rotate():
#     a, b, r = map(int, sys.stdin.readline().rstrip().split())
#     array = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(a)]
#     cut_line = a // 2
#
#     for _ in range(r):
#         n, m = a - 1, b - 1
#         f_n = 0
#         ex_array = deepcopy(array)
#
#         while f_n < cut_line:
#             # 1번, 좌 , 우
#             ex_array[f_n][f_n:m] = array[f_n][f_n + 1:m + 1]
#             ex_array[n][f_n + 1:m + 1] = array[n][f_n:m]
#
#             # 2번, 하, 상
#             cnt = 0
#             for _ in range(n - f_n):
#                 ex_array[f_n + cnt + 1][f_n] = array[f_n + cnt][f_n]
#                 ex_array[f_n + cnt][m] = array[f_n + cnt + 1][m]
#                 cnt += 1
#
#             f_n += 1
#             n, m = n - 1, m - 1
#             array = deepcopy(ex_array)
#
#     return array, a, b
#
#
# array, a, b = rotate()
# s = ''
# for i in range(a):
#     for j in range(b):
#         s += (str(array[i][j]) + ' ')
#     print(s)
#     s = ''

'''
R,f,O=range,lambda:map(int,O().split()),open(0).readline
n,m,r=f()
v=[[*f()]for i in R(n)]
for i in R(min(n,m)//2):
    l=[]
    for a in R(i,n-i):l+=[v[a][i]]
    for b in R(i+1,m-i):l+=[v[a][b]]
    for c in R(a-1,i-1,-1):l+=[v[c][b]]
    for d in R(b-1,i,-1):l+=[v[c][d]]
    j=r%len(l)
    l=iter(l[-j:]+l[:-j])
    for a in R(i,n-i):v[a][i]=next(l)
    for b in R(i+1,m-i):v[a][b]=next(l)
    for c in R(a-1,i-1,-1):v[c][b]=next(l)
    for d in R(b-1,i,-1):v[c][d]=next(l)
for i in v:print(*i)
'''

'''
# 1번, 좌
            for j in range(fc_bc):
                ex_array[fr][j] = array[fr][j + 1]
            # 2번, 하
            for j in range(fr_br):
                ex_array[j+1][fc] = array[j][fc]
            # 3번, 우
            for j in range(fc_bc):
                ex_array[br][j + 1] = array[br][j]
            # 4번, 상
            for j in range(fr_br):
                ex_array[j][bc] = array[j + 1][bc]

'''

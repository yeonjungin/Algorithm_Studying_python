# https://www.acmicpc.net/problem/14467
# from copy import deepcopy
#
# n = int(input())
# array = []
# road = []
#
# for i in range(n):
#     a = list(map(int, input().split()))
#     array.append(a[0])
#     road.append(a[1])
#
# cnt = 0
# answer=0
# index_num_list=[]
# num = 0
#
#
# example_list = deepcopy(array)
# for i in range(1, 11):
#     ex = []
#     if array.count(i) <= 1:
#         continue
#     else:
#         for j in range(n):
#             if example_list.count(i) != 0:
#                 ex.append(example_list.index(i))
#                 example_list[example_list.index(i)] = None
#         index_num_list.append(ex)
#
#
# for a in range(len(index_num_list)):
#     for b in index_num_list[a]:
#         if cnt==0:
#             num=b
#             cnt+=1
#             continue
#         else:
#             if road[b]==road[num]:
#                 num=b
#                 cnt+=1
#             else:
#                 answer+=1
#                 num=b
#                 cnt+=1
#     cnt=0
# print(answer)

l, ct = {}, 0 # 딕셔너리 사용
for i in range(int(input())):
    a, b = map(int, input().split())
    if a not in l: # 처음 리스트에 들어갈 때
        l[a] = b
        print(l)
    # not in , in 연산자 -> 특정한 문자열 안에 찾고자하는 문자열이 있는지 확인하기.
    else: # 중복된 숫자가 있을 경우
        if l[a] != b: # 만약 리스트에 있는 a의 방향과, b의 값이 다르다면? -> 이동횟수 +1
            ct += 1
            l[a] = b
            print(l)
print(ct)
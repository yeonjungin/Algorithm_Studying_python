# n = int(input())
# array = list(map(int, input().split()))
# cnt = 0
# plus = False
# minus = False
# button = False
# mid=False
# answer = 0
#
# for i in range(1, n):
#     if cnt > 1:
#         print(-1)
#         exit()
#     if array[i] >= array[i - 1]:
#         if array[i]==array[i-1]:
#             mid=True
#         plus = True
#         if minus:
#             cnt += 1
#             minus = False
#             plus = True
#             button=True
#         if not button:
#             answer+=1
#     else:
#         minus = True
#         if plus:
#             cnt += 1
#             plus = False
#             minus = False
#             button=True
#
#         if not button:
#             answer+=1
#
# if cnt > 1:
#     print(-1)
# elif cnt == 1:
#     if mid:
#         print(answer)
#     else:
#         print(answer+1)
# else:
#     print(0)
n = int(input())
array = list(map(int, input().split()))
up, down = 1,1
for i in range(1,n):
    if array[i-1]>array[i]:
        break
    up+=1
for i in range(1,n):
    if array[i-1]<array[i]:
        break
    down+=1

upArray = sorted(array)
downArray = sorted(array, reverse=True)
if array == upArray or array == downArray:
    print(0)
elif array[up:] + array[:up] == upArray and array[down:] + array[:down] == downArray:
    print(min(up, down))
elif array[up:] + array[:up] == upArray:
    print(up)
elif array[down:] + array[:down] == downArray:
    print(down)
else:
    print(-1)

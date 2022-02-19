n = int(input())  # n<=50
a = list(map(int, input().split()))  # 원소<=100
b = list(map(int, input().split()))  # 원소<=100
answer=0

for _ in range(n):
    answer+=min(a)*max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))

print(answer)
# n = int(input())  # n<=50
# a = list(map(int, input().split()))  # 원소<=100
# b = list(map(int, input().split()))  # 원소<=100
# visited = [0 for _ in range(n)]
# answer = []
#
#
# # S의 값을 최소화하기 위해 A의 수를 재배열하자. S의 최솟값 출력하기
# def s(new_a):  # 점화식함수
#     temp = 0
#     for i in range(n):
#         temp += new_a[i] * b[i]
#     return temp
#
#
# def func(depth, new_a):
#     if depth == n:
#         answer.append(s(new_a))
#         return
#     for i in range(n):
#         if visited[i]:  # 방문한 적이 있다면?
#             continue
#         visited[i] = 1
#         new_a.append(a[i])
#         func(depth + 1, new_a)
#         visited[i] = 0
#         new_a.pop()
#
#
# func(0, [])
# print(min(answer))
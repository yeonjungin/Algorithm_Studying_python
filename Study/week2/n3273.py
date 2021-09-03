# 1
n = int(input())
array = set(map(int, input().split()))
x = int(input())
cnt = 0

for i in array:
    if x - i in array:
        cnt += 1
print(cnt//2)

# 2
# n = int(input())
# array = list(map(int, input().split()))
# x = int(input())
# cnt = 0
# hash = set()
# for i in array:
#     if i in hash:
#         cnt += 1
#     elif i <= x:
#         hash.add(x - i)
# print(cnt)


# 3
# n = int(input())
# array = sorted(list(map(int, input().split())))
# x = int(input())
#
# left = 0
# right = n - 1
#
# cnt = 0
#
# while left < right:
#     now = array[left] + array[right]
#     if now == x:
#         cnt += 1
#     if now > x:
#         right -= 1
#         continue
#     left += 1
#
# print(cnt)
'''
이 문제는 완탐으로 하게 되면 이중 for문을 써야하므로 시간 복잡도가 N^2가 나온다.
이럴땐 투포인터를 사용하면 리스트가 정렬되어 있을떈 N, 정렬이 되어 있지 않더라도 NlogN으로 위 방식보단 훨씬 효율적이다.
start,end라는 두 개의 포인터를 사용한다.
x=타켓값
'''

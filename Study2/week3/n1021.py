from collections import deque

n, m = map(int, input().split())
array = deque([i for i in range(1, n + 1)])
location = list(map(int, input().split()))

cnt = 0

for i in location:
    if i == array[0]:  # 1번 연산
        array.popleft()
        continue
    else:  # 2번,3번 연산
        if array.index(i) > len(array) // 2:  # 왼쪽으로 이동
            while i != array[0]:
                array.appendleft(array.pop())
                cnt += 1
            array.popleft()
        else:
            while i != array[0]:
                array.append(array.popleft())
                cnt += 1
            array.popleft()
print(cnt)

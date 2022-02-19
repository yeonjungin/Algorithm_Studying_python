from collections import deque

n = int(input())
array = list(map(int, input().split()))
start = int(input()) - 1
visited = [0] * n
result = 0


def bfs(start):  # start=idx
    global result
    queue = deque()
    queue.append(start)
    visited[start] = 1
    result+=1

    while queue:
        node = queue.popleft()
        for i in [-array[node], array[node]]:
            temp = node + i
            if 0 <= temp < n and visited[temp] == 0:
                queue.append(temp)
                result += 1
                visited[temp]=1

bfs(start)
print(result)

'''
1 4 2 2 1 (시작점 idx 2 )
2   -> 왼쪽 1 o
        -> 오른쪽 4 o
             -> x
    -> 오른쪽 1 o
        -> 왼쪽 2 o
            -> 왼쪽 4 0

0의 개수 = 5개
print(5)
'''
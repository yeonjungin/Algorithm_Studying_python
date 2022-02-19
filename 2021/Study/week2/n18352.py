import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
dic = [[] for _ in range(n + 1)]

for i in range(1, m + 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    dic[a].append(b)

queue = deque([x])
visited = [0 for _ in range(n + 1)]
visited[x] = 1
now = 0

while queue:
    node = queue.popleft()

    for i in dic[node]:
        if not visited[i]:
            queue.append(i)
            visited[i] = visited[node] + 1

for i in range(n + 1):
    if visited[i] == k + 1:
        print(i)
if k + 1 not in visited:
    print(-1)


#         if visited[i] == k+1:
#             answer.add(i)
# print(*answer if answer else [-1], sep='\n')

'''
import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
dic = [[] for _ in range(n + 1)]

for i in range(1, m + 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    dic[a].append(b)

queue = deque([x])
visited = [0 for _ in range(n + 1)]
visited[x] = 1
answer = set()
now = 0

while queue:
    node = queue.popleft()

    for i in dic[node]:
        if not visited[i]:
            queue.append(i)
            visited[i] = visited[node] + 1

for i in range(n + 1):
    if visited[i] == k + 1:
        print(i)
        
if k + 1 not in visited:
    print(-1)
'''

'''
백준 5014번 : 스타트링크
https://www.acmicpc.net/problem/5014
'''

'''
총 층수 : f
스타트링크가 존재하는 층 : g
현재 강호의 위치 : s

위 : u
아래 : d
이동할 층이 없으면 엘레베이터는 움직이지 않는다.

강호가 g층에 도착하려면 적어도 몇 번 눌러야 하는가?
g층에 갈 수 없다면, user the stairs를 출력하기

'''
from collections import deque

f, s, g, u, d = map(int, input().split())
graph = [i for i in range(1, f + 1)]

dx = [u, -d]
visited = [0] * f


def bfs(s, f):
    count = 0
    queue = deque()
    queue.append(s)

    while queue:
        x = queue.popleft()
        for i in dx:
            nx = x + i
            if nx > f or nx < 1:
                continue
            if visited[x - 1] == 1:
                continue
            if visited[x - 1] == 0:
                visited[x - 1] = 1
                queue.append(nx)
                count += 1
            if nx == g:
                queue.popleft()
                return count

    return "use the stairs"


print(bfs(s, f))

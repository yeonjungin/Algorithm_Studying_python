from collections import deque

a, b, c = map(int, input().split())
MAX = c
queue = deque()
visited = [[False] * (b + 1) for _ in range(a + 1)]
answer = []


def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        queue.append((x, y))


def bfs():
    queue.append((0, 0))  # a=0, b=0 : 초기상태
    visited[0][0] = True  # a=0이고 b=0일때는 이미 계산했었으니 안해도 되도록 방문처리
    while queue:
        x, y = queue.popleft()
        z = c - x - y  # c 물통에 현재 남아있는 물의 양
        if x == 0:
            answer.append(z)
        # x -> y
        water=min(x,b-y)
        pour(x-water,y+water)
        # x->y로 옮길때 a통에 있는 물의 양 x가 작은지
        # b통에 들어갈 수 있는 물의 양 b-y값이 작은지 판별 후
        # 작은 값을 water에 넣어준다.
        # 물을 넘치게 할 수 없으니까 , a통에 있는 물의 양이 b통에 들어갈 수 있다면?
        # x값이 b-y값보다 작은 것이다.

        # x-> z
        water=min(x,c-z)
        pour(x-water,y)

        # y-> x
        water=min(y,a-x)
        pour(x+water,y-water)

        # y-> z
        water=min(y,c-z)
        pour(x,y-water)

        # z-> x
        water=min(z, a-x)
        pour(x+water,y)

        # z-> y
        water=min(z,b-y)
        pour(x,y+water)



bfs()
print(*sorted(answer))
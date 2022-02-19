from collections import deque

t = int(input())


def bfs():
    queue = deque()
    queue.append([hx, hy])
    while queue:
        nx, ny = queue.popleft()
        if abs(nx - rx) + abs(ny - ry) <= 1000:
            print("happy")
            return
        for i in range(cnum):
            if not visited[i]:  # 아직 방문하지 않음
                cnx, cny = cArray[i]
                if abs(nx - cnx) + abs(ny - cny) <= 1000:
                    queue.append([cnx, cny])
                    visited[i] = 1
    print("sad")
    return


for _ in range(t):
    cnum = int(input())  # 편의점 개수
    beerbox = 20  # 50미터에 1병씩
    hx, hy = map(int, input().split())  # 집
    cArray = [list(map(int, input().split())) for _ in range(cnum)]
    rx, ry = map(int, input().split())  # 페스티벌
    visited = [0 for _ in range(cnum + 1)]
    bfs()

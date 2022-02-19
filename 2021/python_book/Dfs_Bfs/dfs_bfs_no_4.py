'''
p153 미로 탈출 문제
괴물이 있는 곳 0 , 괴물이 없는 부분 1
탈출하기 위해 움직여야 하는 최소 칸의 개수
(칸을 셀 때 시작 칸과 마지막 칸을 모두 포함해서 계산한다)

이 문젠 BFS로 풀어야 유리하다.
BFS는 시작 시점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문이다.

bfs 과정
1. deque 라이브러리를 사용하여 큐 구현
2. 현재 노드를 방문 처리한다.
3. 큐가 빌때까지 해당 과정을 반복한다.
    1. 큐에서 하나의 원소를 뽑아서 출력한다. popleft()
    2. 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입한다.
    3. 해당 원소는 방문 처리 ^^
'''
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))  # 현재 해당 노드 위치
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]


print(bfs(0, 0))

'''
1. 큐 구현을 위해 deque 라이브러리 이용
2. 큐에 현재 해당 노드의 위치를 튜플형태로 저장
3. 큐가 빌 때까지 아래 과정을 반복하기
	1. 큐의 맨왼쪽에서 하나를 꺼내와서 x와 y에 넣어준다.
	2. 현재 위치에서 상하좌우 방향 위치 확인하기
		1. nx에 x+ 방향x값 대입
		2. ny에 y+ 방향y값 대입
		3. nx와 ny의 값이 범위를 넘어서면 continue
		4. graph[nx][ny]의 값이 0 (괴물위치)이면 continue
		5. graph[nx][ny]의 값이 1이면?
			1. graph[nx][ny]에 graph[x][y]+ 1대입
			2. queue에 (nx,ny) 넣기
4. graph[n-1][m-1]값 리턴으로 함수 마무리 :)
'''

'''
바이러스 > 상하좌우 인접한 빈칸으로 이동 가능
새로 새울 수 있는 벽의 개수는 3개 (꼭 3개 세워야한다)
안전 영역 크기 개수 > 0의 개수
'''
from copy import deepcopy

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
virus = []
answer = 0

# 바이러스 리스트를 미리 만들어두기
for i in range(n):
    for j in range(m):
        if array[i][j] == 2:
            virus.append((i, j))


# 벽 선택하기
def wall(start, cnt):
    global answer
    if cnt == 3:  # 벽 3개 선택시
        # 바이러스 퍼트릴거야!
        current_array = deepcopy(array)
        for r, c in virus: # 바이러스가 있는 곳을 중심으로 spread_virus함수 실행
            spread_virus(r, c, current_array)
        # 안전영역 개수 sum(i.count(0) for i in 배열)!!!!
        safe_count = sum(k.count(0) for k in current_array)
        answer = max(answer, safe_count)
        return

    else:  # 벽 선택하는 과정
        for i in range(start, n * m):  # 2차원 배열을 1차원 배열로 계산하는 방법 : for문 줄이기!!
            r = i // m  # 2차원 배열 행 : i // 열의 수
            c = i % m  # 2차원 배열 열 : i % 열의 수
            # start=0이면, r은 0, c는 0
            # start=2이면, r은 0, c는 2
            if array[r][c] == 0:
                array[r][c] = 1  # 벽 선택 과정
                wall(i, cnt + 1)  # 재귀 함수 돌리기
                array[r][c] = 0  # 벽 해제과정


# 바이러스 퍼트리기
def spread_virus(r, c, current_array):
    if current_array[r][c] == 2:  # 바이러스라면?
        # 상하좌우 확인
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if 0 <= nx < n and 0 <= ny < m:  # 범위 안에 있을 경우
                if current_array[nx][ny] == 0:  # 빈 벽일 경우
                    current_array[nx][ny] = 2  # 바이러스로 빈 벽을 채운다.
                    spread_virus(nx, ny, current_array)


wall(0, 0)
print(answer)

# 블럭 종류 : 2가지
# 칸 안에 적힌 숫자의 합이 최대가 되도록 출력
# 이떄, 회전, 뒤집기 모두 가능함.
'''
(풀이)
1. 첫번째, 두번째 블럭에 해당하는 숫자의 값이 최대값인지 확인하는 구문 필요함.
'''

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
answer = 0
# 상, 우, 하
dxs = [-1, 0, 1]
dys = [0, 1, 0]

# 격자 내에 있는지 확인
def can_go(x, y):
    return x >= 0 and x < n and y >= 0 and y < m and not visited[x][y]

# 블럭 안에 적힌 숫자의 합 구하기
def is_ok_block(x, y, cnt):
    if cnt == 2:
        return array[x][y]

    ret = 0
    for i in range(3):
        nx = x + dxs[i]
        ny = y + dys[i]
        if can_go(nx, ny):
            visited[nx][ny] = True
            ret += is_ok_block(nx, ny, cnt + 1)

    return ret


for x in range(n):
    for y in range(m):
        # visited 배열 초기화
        for i in range(n):
            for j in range(m):
                visited[i][j] = False

        # 현재 위치 (x,y) 방문처리
        visited[x][y] = True

        # 블럭 안에 적힌 숫자의 최댓값 구하기
        answer = max(answer, is_ok_block(x, y, 0))

print(answer)


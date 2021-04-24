# 문제 출처 : https://www.acmicpc.net/problem/19236\
# 파이참 단축키 : shift + F10 (실행)

# 단순 2차원 배열은 append로 해도 상관 없다.
# 그러나 2차원 배열 안에 리스트를 넣는 경우엔, 아래처럼 미리 값을 채워두고 바꿔줘야 한다.
from copy import deepcopy

Map = [[None] * 4 for _ in range(4)]
print(Map)
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        Map[i][j] = [data[2 * j], data[2 * j + 1]]
print(Map)
# 이동방향 (상,좌,하,우)
# (-1,0), (-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

result = 0


def dfs(array, x, y, total):
    temp = deepcopy(Map)
    # 현재 위치의 물고기 먹기
    total += temp[x][y][0]
    # 물고기를 먹었으므로 해당 칸에 상어 입장
    temp[x][y][0] = -1 # 상어 방향값은 변경할 필요 x, 기존 값과 동일

    # 물고기 이동 과정
    for i in range(1,17):
        for j in range(4):
            for k in range(4):
                if temp[j][k][0]==i:
                    if temp[j][k]!=None:
                        # 해당 물고기의 현재 좌표, 방향
                        x=j
                        y=k
                        dir=temp[j][k][1]
                        for i in range(8):
                            nx=x+dx[dir]
                            ny=y+dy[dir]
                            if nx>=0 and nx<4 and ny>=0 and ny<4:
                                

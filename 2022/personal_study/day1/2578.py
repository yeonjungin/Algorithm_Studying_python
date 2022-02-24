bingo = []
bingo_dic = {}  # 빙고 숫자 위치 저장 딕셔너리
for i in range(5):
    li = list(map(int, input().split()))
    bingo.append(li)
    for j in range(5):
        bingo_dic[li[j]] = (i, j)  # *****

moderator = [list(map(int, input().split())) for _ in range(5)]
visited = [[0 for _ in range(5)] for _ in range(5)]
answer = 0


def check():
    global answer
    answer=0
    # 가로 줄, 세로 줄 확인
    for i in range(5):
        row, col = 0, 0
        for j in range(5):
            if visited[i][j]:
                row += 1
            if visited[j][i]:
                col += 1
        if row == 5:
            answer += 1
        if col == 5:
            answer += 1
    # 왼쪽 대각선
    left, right = 0, 0
    for i in range(5):
        if visited[i][i]:
            left += 1
        if visited[i][4 - i]:
            right += 1
    if left == 5:
        answer += 1
    if right == 5:
        answer += 1


result = 0
for i in range(5):
    for j in range(5):
        nx, ny = bingo_dic[moderator[i][j]]
        visited[nx][ny] = 1
        result += 1
        check()
        if answer >= 3:
            print(result)
            exit()

bingo_map = [list(map(int, input().split())) for _ in range(5)]
master_map = [list(map(int, input().split())) for _ in range(5)]
visited = [[0 for _ in range(5)] for _ in range(5)]
master_cnt = 0


def cnt_check(bingo_num):
    if bingo_num >= 3:
        return False


def is_check(visited):
    bingo_num = 0
    # 가로
    for x in range(5):
        row = True
        if False in visited[x]:  # 0=False
            row = False
        if row:
            bingo_num += 1

    # 세로 (방법1)
    # col_check=list(map(list,zip(*visited))) #병렬처리 해주는 함수 > zip()함수
    # for x in range(5):
    #     column=True
    #     if False in col_check[x]:
    #         column=False
    #     if column:
    #         bingo_num+=1

    # 세로 (방법2)
    for x in range(5):
        column=True
        if False in visited[:][x]:
            column=False
        if column:
            bingo_num+=1

    # 대각선 (상->하. 하->상)
    diagonal1, diagonal2 = True, True
    for x in range(5):
        if visited[x][x] == 0:
            diagonal1 = False
        if visited[x][4 - x] == False:
            diagonal2 = False

    if diagonal1:
        bingo_num += 1
    if diagonal2:
        bingo_num += 1


    if bingo_num >= 3:
        return True
    return False


final = True
for i in range(5):
    for j in range(5):
        ex_bool = True
        for x in range(5):
            for y in range(5):
                if bingo_map[x][y] == master_map[i][j]:
                    bingo_map[x][y] = 0
                    visited[x][y] = True
                    master_cnt += 1
                    ex_bool = False
                    break
            if ex_bool != True:
                break

        if is_check(visited):
            print(master_cnt)
            final = False
            break

    if final != True:
        break

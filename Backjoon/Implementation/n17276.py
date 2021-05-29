# 17276번 배열 돌리기
import sys

t_num = int(sys.stdin.readline())


# input보다는 sys.stdin.readline.rstrip() rstrip()은 줄바꿈 문자 제외

def plus_turn(array, n):
    num = n // 2
    for i in range(n):
        array[i][i], array[i][num] = array[i][num], array[i][i]
        array[i][i], array[i][n - 1 - i] = array[i][n - 1 - i], array[i][i]
        array[i][i], array[num][i] = array[num][i], array[i][i]

    for i in range(num):
        array[num][i], array[num][n - 1 - i] = array[num][n - 1 - i], array[num][i]

    return array


def minus_turn(array, n):
    num = n // 2
    for i in range(n):
        array[i][n - 1 - i], array[i][num] = array[i][num], array[i][n - 1 - i]
        array[i][n - 1 - i], array[i][i] = array[i][i], array[i][n - 1 - i]
        array[i][n - 1 - i], array[num][i] = array[num][i], array[i][n - 1 - i]

    for i in range(num):
        array[n - 1 - i][i], array[i][n - 1 - i] = array[i][n - 1 - i], array[n - 1 - i][i]
    return array


for _ in range(t_num):
    n, d = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    if d >= 0:
        p_d = d // 45
        for _ in range(p_d):
            array = plus_turn(array, n)
        for i in range(n):
            for j in range(n):
                print(array[i][j], end=' ')
            print()

    else:
        p_d = abs(d) // 45
        for _ in range(p_d):
            array = minus_turn(array, n)
        for i in range(n):
            for j in range(n):
                print(array[i][j], end=' ')
            print()

# for i in range(n):
#     print(*array[i])
# *을 사용하면, 리스트의 대괄호를 제거하고 출력할 수 있다.

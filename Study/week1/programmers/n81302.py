'''
거리두기 확인하기 : Programmers Level 2.
'''
from collections import deque


def bfs(array):
    pass

def solution(places):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    button = True
    answer = []
    queue=deque()
    for array in places:
        button=True
        for i in range(5):
            for j in range(5):
                if array[i][j] == 'P':
                    for k in range(8):
                        ni = i + dx[k]
                        nj = j + dy[k]
                        if ni >= 0 and ni < 5 and nj >= 0 and nj < 5:
                            if array[ni][nj] == 'P':

                if button is False:
                    break
            if button is False:
                break

        if button:
            answer.append(1)
        else:
            answer.append(0)

    return answer

array=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(array))
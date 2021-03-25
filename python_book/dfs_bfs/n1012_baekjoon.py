'''
백준 1012번
https://www.acmicpc.net/problem/1012
'''
import sys

test_n = int(input())
graph = []
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x >= row or x <= -1 or y >= column or y <= -1:
        return
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return


warm_count = 0
count_list = []

for i in range(test_n):
    warm_count = 0
    row, column, num = map(int, input().split())
    graph = [[0 for i in range(column)] for j in range(row)]
    for _ in range(num):
        a, b = map(int, input().split())
        graph[a][b] = 1

    for k in range(row):
        for l in range(column):
            if graph[k][l] == 1:
                dfs(k, l)
                warm_count += 1

    count_list.append(warm_count)


for i in count_list:
    print(i)

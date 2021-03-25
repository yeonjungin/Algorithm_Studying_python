'''
백준 2667번
https://www.acmicpc.net/problem/2667
'''
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

house = []
area = 0

def dfs(x, y):
    global area
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return
    if graph[x][y] == 1:
        area += 1
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return area

count = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append(dfs(i, j))
            count += 1
        area = 0
print(count)
for i in sorted(house):
    print(i)

'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

3 (총 단지수)
7
8
9
(집의 개수 오름차순으로 정렬)
'''

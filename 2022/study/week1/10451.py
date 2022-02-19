import sys
sys.setrecursionlimit(2000)

for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    array.insert(0,0)
    visited = set()
    answer = 0
    idx = 1


    def dfs(node, circle):
        global answer
        if node in circle:
            answer += 1
            return
        if node in visited:
            return
        visited.add(node)
        circle.add(node)
        dfs(array[node],circle)
        circle.remove(node)

    for i in range(1,n+1):
        dfs(array[i], set())

    print(answer)

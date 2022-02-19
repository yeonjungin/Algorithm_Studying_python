import sys
input=sys.stdin.readline

t = int(input())

def dfs(idx, ans):
    visited[idx] = 1
    for temp in array[idx]:
        if not visited[temp]:
            ans = dfs(temp, ans + 1)

    return ans


for _ in range(t):
    n, m = map(int, input().split())
    array = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        # 양방향 그래프
        array[a].append(b)
        array[b].append(a)
    visited = [0] * (n + 1)
    print(dfs(1, 0))

n = int(input())
array = list(map(int, input().split()))
visited = [0 for i in range(n)]
answer = 0
new_array = []


def dfs(cnt, new_array):
    global answer
    if cnt == n:
        answer = max(answer, sum(abs(new_array[i]-new_array[i+1]) for i in range(n-1)))
        return
    for i in range(n):
        if visited[i]: #방문한 곳이라면?
            continue
        visited[i] = 1
        new_array.append(array[i])
        dfs(cnt + 1, new_array)
        visited[i] = 0
        new_array.pop()


dfs(0, new_array)
print(answer)
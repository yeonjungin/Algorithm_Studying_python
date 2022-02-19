# 두사람이 친구 or (A와 친구 and B와 친구인 C가 존재해야한다)
n = int(input())
arr = [input() for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]


# 2-친구가 서로 연결되어 있는지 확인하는 함수
def func(idx, i):
    for a in range(n):
        # b랑 연결된 친구들 개수대로 visited[idx]에 더해줄거야
        if arr[i][a] == "Y" and arr[idx][a] == "Y":
            visited[idx][i] = 1
            return True


# bfs
for idx, temp in enumerate(arr):  # focus num
    for i in range(n):  # moving num
        if i == idx:
            continue
        if arr[idx][i] == "Y" or func(idx, i):  # Y
            visited[idx][i] = 1
            continue


ans=0
for i in visited:
    ans=max(ans,sum(i))

print(ans)


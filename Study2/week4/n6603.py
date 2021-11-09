# k=array[0]
# array[1]~array[7] = 원소 배열

def dfs(array, cnt, temp, i):
    k = array[0]

    if cnt == 6:
        print(*temp)
        return

    for i in range(i, k + 1):
        if visited[i]:  # 방문한 노드
            continue
        visited[i] = 1
        temp.append(array[i])
        dfs(array, cnt + 1, temp, i)
        temp.pop()
        visited[i] = 0


while True:
    array = list(map(int, input().split()))
    visited = [0] * (array[0] + 1)
    if array[0] == 0:
        break
    dfs(array, 0, [], 1)
    print()

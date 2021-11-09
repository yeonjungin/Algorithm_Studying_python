'''
n : 아이스크림 종류
아이스크림 선택 : 3가지
선택하는 방법에 대해 알아보기
'''
n, m = map(int, input().split())
dic = {}
for i in range(1, n + 1):
    dic[i] = []
# dic = {i : [] for i in range(1,n+1)}

for i in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

cnt = 0

def dfs(first,number, depth):
    global cnt
    if depth == 2:
        cnt += 1
        return

    for i in range(number + 1, n + 1):
        if visited[i]:
            continue
        if i in dic[number] or i in dic[first]:
            continue
        visited[i] = 1
        dfs(first,i, depth + 1)
        visited[i] = 0


visited = [0 for _ in range(n+1)]
for i in range(1, n + 1):
    visited[i] = 1
    dfs(i,i, 0)
    visited[i] = 0
print(cnt)

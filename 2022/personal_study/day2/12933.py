inp = list(input())
quack = ['q','u','a','c','k']
len_inp = len(inp)
idx = 0
answer = 0
visited = [False] * len_inp
first = False

if len_inp % 5 != 0 or inp[0] != "q":
    print(-1)
    exit()

for a in range(len_inp):
    if inp[a] == "q" and not visited[a]:  # 방문하지 않았고, q인 곳 -> 시작 구간이다.
        first = True
        for i in range(len_inp):
            if not visited[i] and quack[idx] == inp[i]:
                visited[i] = True
                if inp[i] == "k":
                    if first:
                        answer += 1
                        first = False
                    idx=0
                    continue
                idx += 1
if answer == 0 or not all(visited):
    print(-1)
else:
    print(answer)

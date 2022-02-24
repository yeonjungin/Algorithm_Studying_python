inp_str = list(input())
len_str = len(inp_str)
if len_str % 5 != 0 or inp_str[0] != "q":
    print(-1)
    exit()
quack = "quack"
visited = [False for _ in range(len_str)]
first = False
idx = 0
answer = 0

for x in range(len_str):
    if not visited[x] and inp_str[x] == "q":
        first = True
        for i in range(len_str):
            if not visited[i] and inp_str[i] == quack[idx]:
                visited[i]=True
                if inp_str[i] == "k":
                    if first:
                        answer+=1
                        first=False
                    idx = 0
                    continue
                idx += 1

if not all(visited) or answer==-1:
    print(-1)
    exit()
else:
    print(answer)
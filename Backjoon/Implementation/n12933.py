# https://www.acmicpc.net/problem/12933
duck=input()
word = ['q', 'u', 'a', 'c', 'k']
visited = [False] * len(duck)

cnt = 0
idx = 0
if len(duck) % 5 != 0:
    print(-1)

else:
    for a in range(len(duck)):
        if duck[a] == 'q' and not visited[a]:
            first = True
            for i in range(len(duck)):
                if word[idx] == duck[i] and not visited[i]:
                    visited[i] = True
                    if duck[i] == 'k':
                        if first:
                            cnt += 1
                            first = False
                        idx = 0
                        continue
                    idx += 1

if cnt == 0 or not all(visited):
    print(-1)
else:
    print(cnt)

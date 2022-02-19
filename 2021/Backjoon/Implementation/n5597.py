# https://www.acmicpc.net/problem/5597
submit_list = []
for i in range(28):
    submit_list.append(int(input()))
submit_list.sort()

for _ in range(2):
    submit_list.append(None)

a = 0
for i in range(1, 31):
    if i == submit_list[a]:
        a += 1
        continue
    else:
        print(i)



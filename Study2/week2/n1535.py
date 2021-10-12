'''
1535번. 안녕
'''
import itertools

person = int(input())
loss = list(map(int, input().split()))
smile = list(map(int, input().split()))

joon_health = 100
joon_smile = 0

answer = 0

for i in range(person, 0, -1):
    loss_combi = list(itertools.combinations(loss, i))
    smile_combi = list(itertools.combinations(smile, i))
    for j in range(len(loss_combi)):
        now_sum = sum(loss_combi[j])
        if now_sum > 99:
            continue
        # 기쁨
        answer = max(answer, sum(smile_combi[j]))
print(answer)

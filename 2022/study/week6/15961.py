n, d, k, c = map(int, input().split())
array = list((int(input()) for _ in range(n)))
answer = 0
cache = [0] * (d + 1)
for i in array[:k]:
    if not cache[i]:
        answer += 1
    cache[i] += 1
temp = answer
print(cache)

for i in range(n):
    if answer <= temp:  # answer값 업데이트
        if cache[c]:
            answer = temp
        else:
            answer = temp + 1
    left = array[i]
    right = array[(i + k) % n]
    cache[left] -= 1 # 방문체크
    if not cache[left]: # 현재 리스트에 left 위치에 있는 값이 없는경우
        temp -= 1
    if not cache[right]: # 현재 리스트에 right 위치에 있는 값이 없으면
        temp += 1 # 현재 리스트에 값 추가하는거니까 +1
    cache[right] += 1 # 방문체크

print(answer)

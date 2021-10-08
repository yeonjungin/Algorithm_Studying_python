from itertools import combinations

num = int(input())
array = []
for i in range(num):
    array.append(input())

com_arr = list(combinations(array, 2))
result = 0

for i in com_arr:
    str1, str2 = i[0], i[1]
    visit1 = [0 for _ in range(26)]  # visited1 : ord(str2[k])번째 위치에 str1[k] 요소 넣기.
    visit2 = [0 for _ in range(26)]  # visited2 : 중복체크용,
    cnt = 0

    if len(str1) == len(str2):  # 조건 1) 길이가 같다면
        for k in range(len(str1)):
            a = ord(str1[k]) - ord('a')
            b = ord(str2[k]) - ord('a')
            if not visit1[b]:  # 변환 위치에 알파벳이 비어있을 때
                if visit2[a]: # aa zb인 경우 , a->z , a->b 중복
                    break
                visit1[b] = ord(str1[k])
                visit2[a] = 1
                cnt += 1
                continue

            if visit1[b] == ord(str1[k]):
                cnt+=1
                continue
            else:
                break

    if cnt == len(str1):
        result += 1
print(result)

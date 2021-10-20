n = int(input())
# lambda로 정렬
array = [list(map(int, input().split())) for _ in range(n)]
country_num=array[-1][0]
array = sorted(array, key=lambda x: x[2], reverse=True)
answer = [0] * (country_num+1)
cnt = 0
for i in array:
    if cnt >= 3:
        break
    if answer[i[0]] < 2:
        print(i[0],i[1])
        answer[i[0]] += 1
        cnt += 1
    else:
        continue

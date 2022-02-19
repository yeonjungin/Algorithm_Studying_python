n = int(input())
dic = {}
array = []

for _ in range(n):
    temp = input().split('.')
    if temp[1] in dic:
        dic[temp[1]] += 1
    else:
        dic[temp[1]] = 1 # dic 데이터 추가하는 방식
    array.append(temp[1])

array = list(sorted(set(array)))
for i in array:
    print(i, dic.get(i))

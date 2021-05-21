# 20291. 파일 정리
'''
- 파일의 개수 (확장자별)
- 사전 순으로 정리 (확장자별)
'''

num = int(input())
array = {}
ex_list = []

for _ in range(num):
    b = input().split('.')
    if b[1] in array:  # 해당 key가 딕셔너리 안에 존재하는 지 (in)
        array[b[1]] += 1
    else:
        array[b[1]] = 1
    ex_list.append(b[1])
ex_list = list(sorted(set(ex_list)))

for i in ex_list:
    print(i, array.get(i))

s=set([1,5,1,5,7])
print(list(s))
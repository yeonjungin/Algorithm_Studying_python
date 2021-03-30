'''
p178. 위에서 아래로(실전문제)
- 정렬 x
- 내림차순 정렬해야 함.
'''
n=int(input())
array=[]
for i in range(n):
    array.append(int(input())) # 한 줄당 데이터가 1개일 경우
    # 한 줄에 데이터가 여러개이고, 리스트 형태로 담아야할 경우 사용 array.append(list(map(int, input())))
result=sorted(array,reverse=True) # 내림차순은 sorted(배열,reverse=True)
for i in array:
    print(i,end=' ')
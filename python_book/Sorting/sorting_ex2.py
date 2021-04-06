'''
p180. 성적이 낮은 순서로 학생 출력하기(실전 문제)
- 이 문제는 최대 100,000개까지 입력될 수 있으므로, 최악의 경우 O(NlogN)을 보장하는 알고리즘을 이용하거나,
O(N)을 보장하는 계수 정렬을 이용하면 된다.
'''
n=int(input())
array=[]
for i in range(n):
    input_data=input().split()
    array.append(input_data[0],int(input_data[1]))

array=sorted(array,key=lambda student:student[1])

for student in array:
    print(student[0],end=' ')
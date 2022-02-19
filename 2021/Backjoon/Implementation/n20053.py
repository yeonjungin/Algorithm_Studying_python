# https://www.acmicpc.net/problem/20053
#1
T=int(input())
array=[]
for i in range(T):
    N=int(input())
    array.append(list(map(int,input().split())))

for ex_list in array:
    print(min(ex_list), max(ex_list))


#2
T=int(input())
array=[]
for i in range(T):
    N=int(input())
    array=sorted(map(int,input().split()))
    print(array[0],array[-1])

#3
T=int(input())
array=[]

for i in range(T):
    N=int(input())
    array=list(map(int,input().split()))
    print(min(array), max(array))


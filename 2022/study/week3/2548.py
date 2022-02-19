n=int(input())
array=sorted(list(map(int,input().split())))
a,b=divmod(n,2)
print(array[a+b-1])
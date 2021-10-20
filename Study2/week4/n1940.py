n = int(input())  # 재료 : n개, M (두 재료의 번호를 합쳐서 M이 되어야 갑옷 만들 수 있음)
m = int(input())
array= set(map(int,input().split()))

answer=0
for i in range(n):
    temp=array.pop()
    if m-temp in array:
        answer+=1
print(answer)

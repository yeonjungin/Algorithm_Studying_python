n=int(input())
array=list(map(int,input().split()))
m=int(input())

start=0
end=max(array)
mid=0

while start<=end:
    temp=0
    mid = (start + end) // 2
    for num in array:
        if num<mid:
            temp+=num
            continue
        temp+=mid
    if temp<=m: # 주어진 값보다 작다면, 정수 상한액을 높여줘야한다.
        start=mid+1
    else:
        end=mid-1
print(end)
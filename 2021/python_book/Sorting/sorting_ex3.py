'''
p182. 두 배열의 원소 교체
- 배열 a의 모든 원소의 합이 최대가 되도록 하는 것이다.
- n은 리스트 원소의 개수, k는 바꿔치기 횟수
- 배열 a에서 가장 작은 원소가 배열 b에서 가장 큰 원소보다 작을 때만 교체를 수행

# sorted와 sort의 차이점?
- sorted()는 새로 정렬된 목록을 반환하는데, 원본 리스트는 정렬이 이루어지지 않는다.
- sort()는 원본 리스트까지 정렬하는 것
'''
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]
    else:
        break

print(sum(a))
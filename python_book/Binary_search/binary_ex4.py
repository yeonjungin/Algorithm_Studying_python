# 부품 찾기. p197.
'''
방법1) 이진탐색
방법2) 계수정렬
'''


# 방법1. 이진탐색
'''
def binary_sort(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binary_sort(array, target, start, mid - 1)
        else:
            return binary_sort(array, target, mid + 1, end)
    return None


n = int(input())
array_n = list(map(int, input().split()))
array_n.sort()

m = int(input())
array_m = list(map(int, input().split()))

for i in array_m:
    result = binary_sort(array_n, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
'''

# 방법2. 계수 정렬 이용
'''
n=int(input())
array=[0]*1000001

for i in input().split():
    array[int(i)]=1

m=int(input())
x=list(map(int,input().split()))

for i in x:
    if array[i]==1:
        print('yes',end=' ')
    else:
        print('no',end=' ')
'''

#방법3. 집합 자료형 이용
n=int(input())
array=set(map(int,input().split()))
#set()함수는 집합 자료형을 초기화할 때 사용한다. 단순히 특정한 데이터가 존재하는지 검사할 때 효과적이다.

m=int(input())
x=list(map(int,input().split()))

for i in x:
    if i in array:
        print('yes',end=' ')
    else:
        print('no',end=' ')
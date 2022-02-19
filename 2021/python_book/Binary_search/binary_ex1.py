'''
1. 순차탐색
: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법이다.
보통 정렬되지 않은 리스트에서 데이터를 찾아야할 때 많이 사용한다.
count()메서드도 내부에서 순차탐색이 수행된다.
데이터의 개수가 N개일 때 최대 N번의 비교 연산이 필요하므로 순차 탐색의 최악의 경우 시간 복잡도는 O(N)이다.


2. 이진탐색
: 배열 내부의 데이터가 정렬되어 있을때만 사용 가능한 알고리즘이다.
위치를 나타내는 변수 3개를 사용한다. (시작점, 끝점, 중간점)
찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾아내는 방식이다.
한 번 확인할 때마다 확인하는 원소의 개수가 절반으로 줄어들어서 시간 복잡도는 O(lonN)이다.

이진 탐색 구현 방법 : 재귀함수 이용, 반복문 이용

* 데이터 탐색 범위가 2000만을 넘어가면 이진 탐색으로 문제에 접근해보기
1000만 단위 이상으로 넘어가면 O(logN)의 속도를 내야하는 알고리즘을 떠올려야 한다.
'''

# 재귀함수로 구현한 이진 탐색 소스코드
def binary_search(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2  # 나눈 몫만 구하기 위해 몫 연산자를 구한다. (/는 나누기, %는 나머지 값 구하기)
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

n,target=map(int,input().split())
array=list(map(int,input().split()))

result=binary_search(array,target,0,n-1)
if result==None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)



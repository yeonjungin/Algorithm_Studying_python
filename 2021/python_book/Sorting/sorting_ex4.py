'''
[ 선택 정렬 ]
- 정렬은 이진 탐색의 전처리 과정이다.
- 선택 정렬 : 가장 작은 데이터를 선택해서 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해서 두 번째에 있는 데이터와 바꾸는
이러한 과정들을 N-1번 반복하는 과정이다.
- 선택 정렬의 시간 복잡도는 O(N^2) : 연산횟수는 N+N-1+....2니까, N*(N+1)/2 = (N^2+N)/2
    이중 반복문이 사용되었으니까, O(N^2)
'''
# EX1 선택 정렬 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):  # 위치를 옮긴 작은 데이터들 다음 인덱스부터 반복을 시작하게 하는 역할
    min_index = i
    for j in range(i + 1, len(array)):  # 이 과정을 통해 가장 작은 값의 인덱스를 찾아낸다.
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 교환 (파이썬 스와프 과정)
print('EX1 >', array)

'''
[ 삽입 정렬 ]
- 구현 난이도 : 선택 정렬(쉬움) > 삽입 정렬(어려움)
- 실행 속도 측면 : 선택 정렬(느림) < 삽입 정렬(빠름)
- 삽입 정렬은 특정한 테이터를 적절한 위치에 삽입한다는 의미로, 데이터가 정렬되어 있을 때 훨씬 효율적인 방법론이다.
- 삽입 정렬은 두 번째 데이터부터 탐색 시작! (첫 번째 데이터는 정렬되어 있다고 가정하기 때문이다)
- 삽입 정렬의 시간 복잡도는 O(N^2), 최선의 경우는 O(N) -> 데이터가 정렬되어 있는 경우
- 보통 삽입 정렬이 퀵 정렬보다는 비효율적인데, 데이터가 정렬되어 있을 땐 퀵 정렬보다 더 강력하다.
'''
# EX2 삽입 정렬 소스 코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
print('EX2 >', array)

'''
[ 퀵 정렬 ]
- 가장 많이 사용 되는 정렬 = 퀵 정렬!
- 기준을 설정한 다음 큰 수와 작은 수를 교환하고, 리스트를 반으로 나누는 방식이다.
- 피벗이 사용된다. (큰 수와 작은 수 교환시 기준이 되는 숫자)
- 동작 설명 
    PART1
    1. 피벗을 설정한다.
    2. 피벗을 기준으로 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.
    3. 값을 찾았으면 큰 데이터와 작은 데이터의 위치를 서로 바꿔준다.
    ( 왼쪽의 값이 피벗보다 작고, 오른쪽의 값이 피벗보다 클 경우에는 작은 데이터와 피벗의 위치를 변경한다. = 분할완료되는 바로 직전 시점)
    PART2
    1. PART1과 동일한 방식으로 왼쪽 리스트에서도 작업을 수행한다.
    PART3
    1. PART1과 동일한 방식으로 오른쪽 리스트에서도 작업을 수행한다.
- 퀵 정렬은 재귀함수로 작성하면 매우 코드가 간결해진다.
- 퀵 정렬 재귀함수의 종료조건은 현재 리스트의 데이터 개수가 1개일 때!
- 퀵 정렬의 시간 복잡도는 O(NlogN)이다. 최악의 경우 O(N^2) => 이미 데이터가 정렬되어 있는 경우에 해당
'''
# EX3 퀵정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print('EX3 > ', quick_sort(array))

'''
[ 계수 정렬 ]
- 특정한 조건이 부합할 때만 사용할 수 있지만, 매우 빠른 알고리즘이다.
- 최악의 경우에도 O(N+K)를 보장한다. | N은 데이터의 개수, k는 데이터 중 최대값의 크기
- 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용할 수 있다.
왜 크기제한이 있을까~? : 모든 범위를 담을 수 있는 리스트를 선언해야 하기 때문이다.
- 별도의 리스트를 선언하고, 그 안에 정렬에 대한 정보를 담는다.
-  동일한 값을 가지는 데이터가 여러 개 등장할 때 적합하다.
- 데이터의 특성 파악이 어려울 경우엔 무조건 그냥 퀵 정렬 사용해보자
'''
# EX4. 계수 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
print()

'''
[파이썬 정렬 라이브러리]
1. sorted()
: 퀵 정렬과 동작 방식이 비슷한 병합 정렬로 이루어져있고, 최악의 시간 복잡도는 O(NlogN)
'''
# EX5. sorted()
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = sorted(array)
print(result)

# EX6. sort()
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array.sort()
print(result)

# EX7. key를 활용
array=[('바나나', 2), ('사과', 3), ('당근', 3)]


def setting(data):
    return data[1]


result = sorted(array, key=setting)
print(result)

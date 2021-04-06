# 떡볶이 떡 만들기. 201p
'''
떡의 길이가 일정하지 않다, 손님이 요청한 총 길이 M
적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값 구하기

(해설)
이 문제는 전형적인 이진 탐색 문제이고, 파라메트릭 서치 유형의 문제이다.
원하는 조건을 만족하는 가장 알맞는 값을 찾는 문제에 주로 파라메트릭 서치를 사용함.
보통 파라메트릭 서치 유형은 이진탐색을 사용하여 해결한다.

적절한 높이를 찾을때까지 절단기의 높이 H를 반복해서 조정한다.
'''

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m: #만약 떡의 길이가 부족하다면, 왼쪽 부분을 탐색하여 떡의 총길이를 늘린다.
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

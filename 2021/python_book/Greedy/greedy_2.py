'''
Chaper3 Greedy(탐욕법) 문제 풀이 및 내용정리
02. 숫자 카드 게임
'''

# 방법1 : min 함수 이용

n, m = map(int, input().split())
result = 0

for i in range(n):  # 한 줄씩 입력받기, 행에서 가장 작은 수를 골라내기 위함
    data = list(map(int, input().split()))
    min_data = min(data)  # 행에서 가장 작은 수를 min_data에 저장
    result = max(result, min_data)  # result와 min_data중 큰 수를 result 변수에 저장
print(result)


# 방법2 : for문 활용

n, m = map(int, input().split())
result=0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10000
    for j in data:
        min_value = min(min_value, j)
    result += max(result, min_value)
print(result)

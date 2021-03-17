'''
Chaper3 Greedy(탐욕법) 문제 풀이 및 내용정리
01. 큰 수의 법칙
'''

# map (function, iterable,...)
# iterable의 모든 항목에 function을 적용한 후 결과를 돌려주는 이터레이터를 돌려준다.
# map 객체는 이터레이터라서 변수 여러 개에 저장하는 언패킹이 가능하다.

'''
데이터 입력 받는 방법 정리!
(1) 1개의 데이터 입력받기
n=int(input())

(2) 각 데이터를 공백으로 구분하여 입력받기
list(map(int,input().split())의 동작과정
1. input()으로 문자열을 입력받는다.
2. 입력받은 문자열을 split()을 통해 공백으로 나눈 리스트로 바꾼다.
3. map을 이용하여 해당 리스트의 모든 원소에 int()함수를 적용한다.
4. 최종적으로 결과를 list()로 다시 바꿔서 각각 숫자 자료형으로 저장하게 된다.

(3) 공백을 기준으로 구분하여 적은 수의 데이터 입력
n,m,k=map(int,input().split())

(4) 입력의 개수가 많은 경우, input()을 사용하지 않는다.
input()함수는 속도가 느려서 시간 초과로 오답 판정을 받을 수 있기 때문이다.
따라서 파이썬의 sys 라이브러리에 저장되어 있는 sys.stdin.readline()함수를 이용한다.

(5) 여러 줄의 데이터를 입력받기
array=[]
for i in range(n): n은 행의 수
    array.append(list(map(int,input().split())))
    
import sys
sys.stdin.readline().rstrip()

# readline으로 입력하면 입력 후 엔터가 줄바꿈 기호로 입력되는데, rstrip()을 이용하여 이를 제거한다.
'''

# 방법1
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

first = data[n - 1]
second = data[n - 2]
n_sum = 0

while True:
    if m == 0:
        break
    else:
        for i in range(k):
            n_sum += first
            m -= 1
        n_sum += second
        m -= 1
print(n_sum)

# 방법2
# 반복되는 수열에 대해 파악을 먼저 해야 한다.
n,m,k=map(int,input().split())
data2=list(map(int,input().split()))

data2.sort()
first2=data[n-1]
second2=data[n-2]

count=int(m/(k+1))*k # 가장 큰 수가 더해지는 횟수
count+=m%(k+1) # 수열의 개수가 딱 떨어지지 않을 경우까지 대비

result=0
result+=count*first2
result+=(m-count)*second2

print(result)
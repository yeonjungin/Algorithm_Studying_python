'''
Chaper3 Greedy(탐욕법) 문제 풀이 및 내용정리
03. 1이 될 때까지
'''

# 내가 생각해낸 방법
'''
n, k = map(int, input().split())
result = 0
while True:
    if n == 1:
        break
    else:
        if n % k == 0:
            n = n // k
            result += 1
        else:
            n -= 1
            result += 1
print(result)
'''
# 책 풀이
# k로 최대한 많이 나눌 수 있도록 하는 것이 최적의 해를 보장한다.
'''
N의 범위가 100억 이상이면, 위 풀이는 시간이 오래 걸린다. 1을 매번 빼줘야 하기 때문
그래서 아래와 같은 코드로 작성을 한다.
ex) n=100, k=30
1. n 이하인 수 중에서 n과 가장 가까운 k의 배수를 찾는다. (ex) target에는 90이 저장된다. 
2. 100에서 90을 빼준다 (ex) result에는 10이 저장된다.
>> 1을 매번 빼주는 과정들을 한 번에 처리해주는 과정에 속한다.
원래대로라면 1을 빼고 for문을 돌아서 또 나누고 해야하는데, 
위와 같이 최대한 많이 나누기를 수행해주면 수행속도가 더 빨라진다.
3. n에 target 값을 넣어준다. (ex) n에는 90이 저장된다.
4. 만약 n의 값이 k값 보다 작다면 반복문을 빠져나와야 한다.
5. n의 값이 k값과 같거나 크면 result에는 +1을 해준다. (ex) result는 11
>> n의 갑이 k의 값에 떨어지는 과정의 횟수도 더해줘야 하니까!
6. n의 값에 n//k의 값을 넣어준다 (ex) n=90//30=3 
7. 이 과정을 반복하다가 n의 값이 k보다 작아지면 반복문에서 빠져나옴
8. 마지막으로 남아있는 수에 대해 1씩 빼기 (1이 될 때까지)

n, k = map(int, input().split())
result = 0
'''
n,k=map(int,input().split())
result=0
while True:
    target = (n // k) * k  # n과 가까운 배수를 찾는 과정
    result += (n - target)  # n이 target이 될 때까지 1씩 빼주는 것
    n = target
    if n < k:
        break
    result += 1
    n //= k
    print("target: {} , result : {}, n : {}".format(target, result, n))
result += (n - 1)
print(result)
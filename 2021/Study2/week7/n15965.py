'''
에라토스테네스의 체 :  합성수를 지우는 방식으로 소수를 찾는 방법


'''
k = int(input())
array = [1 for _ in range(10000001)]
answer = []
for i in range(2, 10000001):
    if array[i]:
        answer.append(i)
        for j in range(i * 2, 10000001, i):
            if j > 10000000:
                break
            array[j] = 0
print(answer[k-1])

#https://wikidocs.net/21638
n, w = map(int, input().split())
array = [0 for _ in range(n)]
for i in range(n):
    array[i] = int(input())

'''
매도 : 가격이 가장 비쌀 때
매수 : 가격이 가장 쌀 때
'''

coin = 0  # 현재 코인 개수
cash = 0  # 현재 현금 금액
button = True  # True : up, False : down

for day, price in enumerate(array):
    if day == 0:
        coin += w // price
        cash += w % price

    if day == n - 1:  # 모든 코인 매수
        cash += coin * price
        print(cash)
        exit(0)

    if array[day] <= array[day + 1]:  # 매수 매도 x, 위로 올라가는 과정, 최대 꼭짓점 찾아가는 과정
        if button == False: # 현재 내려가던 중이었는데 다음 인덱스부터 금액이 다시 올라가는 경우 = 매수시점
            # 매수
            coin += cash // price
            cash -= coin * price
        button = True  # up-button up
        continue

    # 내려가는 과정 (최소 꼭짓점 찾아가는 과정)
    elif array[day] >= array[day + 1]:
        if button == True: # 현재 금액이 올라가는 상승곡선이었는데 다음 인덱스부터 금액이 다시 내려가는 경우 = 매도시점점
           # 매도
            cash += price * coin
            coin = 0
        button = False
        continue

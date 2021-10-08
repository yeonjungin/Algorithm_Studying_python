money = int(input())
array = list(map(int, input().split()))


# 준현
def BNP(money, array):
    count = 0  # 주식 수
    for today in range(len(array)):
        temp = money // array[today]
        money -= temp * array[today]
        count += temp
    money += count * array[-1]
    return money


# 성민
def TIMING(money, array):
    up_cnt = 0  # 상승 연속체크
    down_cnt = 0  # 하락 연속체크
    count = 0  # 주식 수

    for today in range(1, len(array)):
        temp = money // array[today]  # 살 수 있는 주식의 수

        if array[today - 1] < array[today]:  # 주가 상승
            down_cnt = 0
            up_cnt += 1
            if up_cnt >= 3:  # 전량 매도
                money += count * array[today]
                count = 0
            continue

        if array[today - 1] > array[today]:  # 주가 하락
            up_cnt = 0
            down_cnt += 1

            if down_cnt >= 3:  # 전량 매수
                money -= temp * array[today]
                count += temp

    money += count * array[-1]
    return money


h = BNP(money, array)
s = TIMING(money, array)

if h > s:
    print("BNP")
elif h == s:
    print("SAMESAME")
else:
    print("TIMING")

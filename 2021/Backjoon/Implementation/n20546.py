money = int(input())
array = list(map(int, input().split()))

# 준현이는 무조건 매수, 그리고 안 판다.
# 성민이는 33 매매법, 현금>주가, 3일 연속 가격이 상승하면 전량 매도, 전날과 오늘날 주가 동일하면 판매x
# 3일 연속 하락하는 건 즉시 주식을 전량매수,
# 1월 14일의 자산 : 현금 + 1월 14일의 주가 * 주식 수
hyeon = money
hyeon_cnt = 0

sung = money
sung_cnt = 0

up = 0 # 가격상승 횟수 세기 위한 변수
down = 0 # 가격하락 횟수 ...

# 준현이의 매수매도
for i in array:
    if i > hyeon:
        continue
    else:
        hyeon_cnt += hyeon // i
        hyeon = hyeon % i

# 성민이의 매수매도
for i in range(len(array) - 1):
    if array[i] > array[i + 1]:  # 만약 값이 하락했다면, 매수
        if up > 0:
            up = 0
            down += 1
        else:
            down += 1
            if down >= 3 and sung // array[i + 1] > 0:
                sung_cnt += sung // array[i + 1]
                sung = sung % array[i + 1]
    elif array[i] < array[i + 1]:  # 만약 값이 상승했다면, 매도
        if down > 0:
            down = 0
            up = 1
        else:
            up += 1
            if up >= 3 and sung_cnt > 0:
                sung += sung_cnt * array[i + 1]
                sung_cnt = 0
    else: # 값이 같다면, 초기화 시킨다.
        down = 0
        up = 0

if sung + sung_cnt * array[-1] > hyeon + hyeon_cnt * array[-1]:
    print("TIMING")
elif sung + sung_cnt * array[-1] < hyeon + hyeon_cnt * array[-1]:
    print("BNP")
else:
    print("SAMESAME")

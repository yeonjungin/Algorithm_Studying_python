# 1/12일
n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]

left = min(array)
right = sum(array)
answer = sum(array)  # 최댓값

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    money = 0
    button = False

    for now in array:
        if mid - now < 0:
            # 출금하더라도 이용할 금액에 미치지 못하는 경우
            # K원 < 이용금액
            button = True
            break
        if money - now < 0:
            money = mid
            cnt += 1
        money -= now

    if not button:
        if cnt > m:
            left = mid + 1
        else:
            right = mid - 1
            answer = min(mid, answer)
    else:
        # K원<이용 금액이므로 k원의 값을 올려줘야한다.
        # 따라서 left=mid+1로 변경해줌으로써 mid(k)의 값을 올려준다.
        left = mid + 1
print(answer)
'''
N일 동안, M번만 돈을 뺸다. (M번만 빼야한다)
k>=이용금액 -> 0
현재 가지고 있는 돈 < 오늘 써야하는 금액 -> 현재 가지고 있는 돈을 통장에 넣고, k원을 출금 

'''

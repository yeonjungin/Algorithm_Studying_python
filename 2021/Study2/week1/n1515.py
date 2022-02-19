# 수 이어쓰기
'''
1~9 : 9개
10~99 : 2*10*9=180 (2자리수 * 10~20 = 10개 * 10~90 => 9개)

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
1111111
1 10 11 12 13 14
1 1  11 1  1  1

82340329923 -> 43
8 12 13 14 20 23 29 39 42 43
1~3000까지 비교하는 거

현재가 23이야, 근데 다음 숫자가 22야, 작으면 안되니까 다음 숫자를 봐, 29야 그러면 29로 하고 2칸 앞으로 가는거야
만약 23보다 작은숫자면 32겠지?

32098221 => 61
3 12 20 29 38 42 52 61
'''
answer = []
temp = input()
i = 0
while True:
    i += 1
    num = str(i)
    while len(num) > 0 and len(temp) > 0:  # num과 temp가 비어있지 않는 경우에만 while문 돌아간다.
        if num[0] == temp[0]:
            temp = temp[1:]
        num = num[1:]  # num이 112인데, temp[0]이 1이 아니면, num은 12, 2로 되고 다시 while문 돌아간다.
        print(num)
    if temp == '':
        print(i)
        break

# d = [a for a in list(map(int, str(j))) if a in temp[i:i + len(str(j))]]

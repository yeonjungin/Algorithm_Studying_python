n = int(input())
cnt = 0
temp = n % 5  # 나머지

if n == 1 or n == 3:
    print(-1)
    exit(0)

elif temp % 2 == 0:  # 2로 딱 떨어지면
    cnt = n // 5 + temp // 2
    print(cnt)
    exit(0)

else:
    cnt = n // 5 - 1 + (temp + 5) // 2
    print(cnt)
    exit(0)
'''
동전의 개수가 최소?
11 12 13 14 15 16 17 18 19 20 => 5랑 2로 다 떨어짐
1이랑 3만 안 될뿐

17 
5원 * 3개 , 2원 * 1개

13
5원 * 2개 x
5원 * 1개, 2원 * 4개

11
5원 * 2개 , 2원 * 1개 , 1이 초과된다 x
5원 * 1개 , 2원 * 3개
'''

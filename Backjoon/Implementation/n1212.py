# 1212번. 8진수 2진수
# 문제 출처 : https://www.acmicpc.net/problem/1212
# 8진수 -> 10진수, 10진수 -> 2진수
# b=int(input(),8)
# print(bin(b)[2:])

def change(num, first = False):
    ret = ''  # 문자열 초기화
    while num:
        ret += chr(num % 2 + 48) #아스키코드, 48 : '0', 49 :'1'
        num //= 2
    while len(ret) < 3: # 3자리 이하면, 오른쪽 끝에부터 '0' 추가
        ret += '0'

    idx = 3
    if first: # 맨 처음 숫자일 때 (0b 제거작업)
        while idx > 1 and ret[idx - 1] == '0':
            idx -= 1
    return ret[:idx][::-1]

N = input()
isFirst = True # 0b를 없애주기 위해 필요한 변수
# 8진수 314를 2진수로 변환하기 위해서는, 3 | 1 | 4 각각 나눠준 뒤, 3을 2진수로, 1을 2진수로 바꿔주면 끝!
for i in range(len(N)):
    print(change(int(N[i]), isFirst),end='')
    isFirst = False #처음에만 작동하고, 그 이후엔 작동 x

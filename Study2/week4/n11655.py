'''
a = 65 > +13 > 78 = n
65 + 25개 -> 90까지
알파벳 대문자 : 65~90
알파벳 소문자 : 97~122
'''
temp = input()
answer = ''

for idx, i in enumerate(temp):
    i = ord(i)
    if 65 <= i <= 90:  # 대문자
        if i > 90:
            i -= 26
            answer += chr(i)
            continue
        else:
            answer += chr(i)

    elif 97 <= i <= 122:
        i += 13
        if i > 122:
            i -= 26  # 알파벳 총개수를 빼주면 앞으로 넘어감
            answer += chr(i)
            continue
        else:
            answer += chr(i)
    else:
        answer += chr(i)

print(answer)
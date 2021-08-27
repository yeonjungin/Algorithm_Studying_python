'''

알파벳 소문자, 공백, 숫자, 특수문자
태그
    길이가 3이상인 부분 문자열
    < > 사이에 소문자, 공백만 가능
단어
    소문자, 숫자
연속하는 두 단어
    공백으로 구분
태그와 단어
    사이에 공백이 없음

단어만 뒤집는다.

'''
# 다른 코드
sentence=input().replace('>','<').split('<')
# print(sentence)
# <problem>17413<is hardest>problem ever<end>
# ['', 'problem', '17413', 'is hardest', 'problem ever', 'end', '']
answer=''
for i in range(len(sentence)):
    if i%2: # 태그
        answer+='<'+sentence[i]+'>'
    else: # 단어의 인덱스는 항상 2의 배수
        word=sentence[i].split()
        answer+=' '.join([x[::-1] for x in word])
print(answer)


# 내 코드
# sentence = input()
# state = True
# answer = ''
# word = ''
#
# for i in range(len(sentence)):
#     if sentence[i] == '<': # <일 경우
#         if word != '': # 만약 단어일경우
#             answer += word[::-1]
#             answer += '<'
#             state = False
#             word = ''
#             continue
#         state = False
#         answer += '<'
#         continue
#
#     if sentence[i] == '>': # >일 경우
#         state = True
#         answer += word[::-1]
#         answer += '>'
#         word = ''
#         continue
#
#     if sentence[i] == ' ': # 공백일 경우
#         answer += word[::-1]
#         answer += sentence[i]
#         word = ''
#         continue
#
#     if not state:  # 태그
#         answer += sentence[i]
#
#     else:  # 단어
#         if i == len(sentence) - 1:
#             word += sentence[i]
#             answer += word[::-1]
#             break
#         word += sentence[i]
#
# print(answer)

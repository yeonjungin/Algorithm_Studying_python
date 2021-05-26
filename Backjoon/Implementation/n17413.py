# 17413번. 단어 뒤집기 2
'''
(문제 풀이 생각 적기)
주의해야할 조건
1. <> 단어 <> : 단어만 반대로 >> 꺽새 안에 있는 단어는 x
2. 공백을 기준으로 단어 나눈다.
3. 태그와 단어 사이에는 공백이 없다.
4. 태그 안에 단어가 달라도 상관없음. <> 이것만 체크하면 된다.

꺽새가 있는 경우, 없는 경우
꺽새가 없으면, array 단어만 반대로 해서 출력하면 된다.
꺽새가 있으면, 꺽새 갯수에 따라 단어를 인식하고, 그 단어만 뒤집어서 제출하면 됌

'''
# 1
string = input().replace('>', '<').split('<')
# replace("찾을 값","바꿀 값",바꿀횟수)
print(string)
result = ""
for i in range(len(string)):
    if i % 2 == 1:  # 꺽새 안에 있는 문자의 인덱스는 항상 2의 배수
        result += '<' + string[i] + ">"
    else:
        temp = string[i].split()
        result += ' '.join([word[::-1] for word in temp])
print(result)



# 2
import sys

ex_word = ''
answer = ''
state = False

word = list(sys.stdin.readline().strip())

for i in word:
    if state == False:
        if i == "<":
            state = True
            ex_word += i

        elif i == " ":
            ex_word += i
            answer += ex_word
            ex_word = ''
        else:
            ex_word = i+ex_word
    else:
        ex_word += i
        if i == '>':
            state = False
            answer += ex_word
            ex_word = ''

print(answer+ex_word)

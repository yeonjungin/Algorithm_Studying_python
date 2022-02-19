'''
Chapter4 구현
실전문제2. 왕실의 나이트

1. 입력값 받기
2. 입력값이 a1인지 1a인지 모르니까, 이를 가려내는 조건문을 실행해서 row,column값에 각각 알맞게 저장함
# ord(c)는 문자의 아스키 코드값을 돌려주는 함수 <-> chr(i)는 아스키 코드값을 문자열로 돌려주는 함수
3. 이동할 수 있는 방향 총 8가지를 steps라는 리스트에 정리해서 저장하기
4. result 변수 선언
5. next_row는 step에 나와있는 방향대로 움직였을때의 행값
마찬가지로 next_column은 step에 나와있는 방향대로 움직였을때의 열값
6. 만약 next_row와 next_column의 값이 1이상이고 8이하이면, 이동이 가능하다는 거니까
result에 +1씩 더해준다.
'''

input_data = input()
if int(ord(input_data[0])) >= 97:
    row = int(input_data[1])
    column = int(ord(input_data[0])) - int(ord('a')) + 1
else:
    row = int(input_data[0])
    column = int(ord(input_data[1]) - int(ord('a')) + 1)

steps=[(-2,-1),(-2,1),(-1,2),(1,2),(2,-1),(2,1),(-1,-2),(1,-2)]
# U, R, D, L 순서 (왼쪽, 위쪽 우선순위)
result=0

for step in steps:
    next_row=step[0]+row
    next_column=step[1]+column
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
        result+=1

print(result)
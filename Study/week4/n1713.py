'''
1. 비어있는 경우
2. 비어있는 사진들이 없는 경우 
    - 추천횟수가 적은 학생의 사진 삭제
    - 그 자리에 새로 들어간다. 
        - 만약 추천횟수가 적은 학생이 두명 이상이면, 가장 오래된 사진
    우선순위 : 추천횟수 > 게시순
3. 현재 사진이 게시된 학생이 추천받은 경우 - 추천 받은 횟수만 증가
'''

photo_n = int(input())  # n
recommend_n = int(input())  # w
input_list = list(map(int, input().split()))  # num
photo_dic = dict()  # photo

# 키 : 후보자이름, 값 : [추천수,들어온순서]
for i in range(recommend_n):
    if input_list[i] in photo_dic:
        photo_dic[input_list[i]][0] += 1
    else:
        if len(photo_dic) < photo_n:
            # 사진틀 꽉 차지 않았을때
            photo_dic[input_list[i]] = [1, i]
        else:
            # 사진이 꽉 차있을 때
            del_list = sorted(photo_dic.items(), key=lambda x: (x[1][0],x[1][1]))
            del_key = del_list[0][0]
            del (photo_dic[del_key])
            photo_dic[input_list[i]] = [1, i]

answer_list = list(sorted(photo_dic.keys()))
answer = ""
for i in answer_list:
    print(i,end=' ')

# https://www.codetree.ai/missions/2/problems/number-of-happy-sequence/description
n,chk=map(int,input().split()) # 격자 크기 n, 연속해야 하는 숫자의 수 : n
array=[list(map(int,input().split())) for _ in range(n)]
result=0

for i in range(n):
    # 행별로 체크
    cnt_row=0
    cur_chk_row=array[i][0]
    for j in range(n):
        # 연속하는 수에 해당하는 경우
        if array[i][j]==cur_chk_row:
            cnt_row+=1
        # 연속하는 수에 해당하지 않는 경우
        else:
            cnt_row=1
            cur_chk_row=array[i][j]
        # 연속해야 하는 숫자의 수를 만족한 경우
        if cnt_row==chk:
            result+=1
            break
    # 열별로 체크
    cnt_col=0
    cur_chk_col=array[0][i]
    for j in range(n):
        # 연속하는 수에 해당하는 경우
        if array[j][i]==cur_chk_col:
            cnt_col+=1
        # 연속하는 수에 해당하지 않는 경우
        else:
            cnt_col=1
            cur_chk_col=array[j][i]
        # 연속해야 하는 숫자의 수를 만족한 경우
        if cnt_col==chk:
            result+=1
            break
print(result)
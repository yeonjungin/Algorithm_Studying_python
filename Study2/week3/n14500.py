n,m=map(int,input().split()) # 열 n, 행 m
array=[list(map(int,input().split())) for _ in range(m)]
print(array)

# 회전 휴리스틱
# 대칭 휴리스틱

'''
5번 반복 ( 테트로미노 가지수가 5개니까)
정방향 최댓값 => 90도 회전 방향 최댓값 -> 180도 회전 방향 최댓값 -> 270도 회전 방향 최댓값 중 max 구해서 넣기
'''
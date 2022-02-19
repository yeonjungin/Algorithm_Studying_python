'''

근접한 햄버거부터 먹게끔 for문 돌리기
k=3이면 1부터 시작해서 근처에 햄버거가 없을 경우 2로 넘어가는 방식?
'''
n, k = map(int, input().split())
array = list(input())
answer = 0

for i in range(n):
    if array[i] == "P":  # 사람
        for j in range(max(i - k, 0), min(n, i + k + 1)):
            if array[j] == "H":
                answer += 1
                array[j] = 0
                break

print(answer)

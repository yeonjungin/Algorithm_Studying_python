def func(num):
    global array, n,m
    # 1번 연산 -> 배열을 상하반전
    if num == 1:
        temp = []
        for i in range(n):
            temp.append(array[n - 1 - i])
        array = temp
        del temp
        return
    # 2번 연산 -> 배열 좌우반전
    if num == 2:
        temp = []
        for i in range(n):
            temp.append(array[i][::-1])
        array = temp
        del temp
        return
    # 3번 연산 -> 오른쪽으로 90도 회전
    if num == 3:
        temp = [[] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                temp[i].append(array[n-1-j][i])
        array = temp
        del temp
        n=len(array)
        m=len(array[1])
        return
    # 4번 연산 -> 왼쪽으로 90도 회전
    if num == 4:
        temp = [[] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                temp[i].append(array[j][m-1-i])
        array = temp
        del temp
        n = len(array)
        m = len(array[1])
        return
    # 5번 연산과 6번 연산은 4개의 부분 배열로 나눠야한다 (n/2 X m/2)
    # 5번 연산 -> (1번->2번, 2번->3번, 3번->4번, 4번->1번)
    if num == 5:
        temp = [[] for _ in range(n)]
        for i in range(n//2):
            for j in range(m // 2):
                temp[i].append(array[n//2+i][j]) # 4->1
            for j in range(m // 2):
                temp[i+n//2].append(array[n//2+i][m//2+j]) # 3->4
            for j in range(m // 2):
                temp[i].append(array[i][j]) # 1->2
            for j in range(m // 2):
                temp[i+n//2].append(array[i][m//2+j])# 2-> 3
        array=temp
        del temp
        return
    # 6번 연산 -> (1번 ->4번, 4번 -> 3번, 3번 ->2번, 2번 -> 1번)
    if num == 6:
        temp = [[] for _ in range(n)]
        for i in range(n // 2):
            for j in range(m // 2):
                temp[i].append(array[i][j+m//2])  # 2 -> 1
            for j in range(m // 2):
                temp[i + n // 2].append(array[i][j])  # 1 -> 4
            for j in range(m // 2):
                temp[i+n//2].append(array[i+n//2][j])  # 4->3
            for j in range(m // 2):
                temp[i].append(array[i+n//2][m // 2 + j])  # 3->2
        array = temp
        del temp
        return


n, m, r = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
cnt = list(map(int, input().split()))
for i in range(r):
    func(cnt[i])

for i in range(len(array)):
    print(*array[i])


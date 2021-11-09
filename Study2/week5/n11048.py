# n, m = map(int, input().split())
# array = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0 for _ in range(m+1)] for _ in range(n + 1)]
#
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         dp[i][j] = array[i - 1][j - 1] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
#
# print(dp[n][m])
# 문서 번호, 인쇄 요청 시각, 페이지 수
# 페이지 수가 적은 문서 -> 먼저 요청된 문서
# (현재 인쇄중인 문서 끝난 시각 == 새로 요청된 문서의 인쇄 요청 시각)
# -> 새로 요청된 문서를 먼저 대기열에 추가 후 다음에 인쇄해야 될 문서 선택
data = [[1, 0, 5], [2, 2, 2], [3, 3, 1], [4, 4, 1], [5, 10, 2]]
standby = []
answer = set()
print = []
time = 0


def page(data):
    data = sorted(data, key=lambda x: x[2])
    return data


def firstDocument(data):
    data = sorted(data, key=lambda x: x[1])
    return data


def add(data, new):
    data.append(new)
    return data


data = firstDocument(data)
print = data.pop(0)
time = print[1]
answer.add(print[0])

while data:
    temp = data.pop(0)
    if not print or not standby:
        answer.add(temp[0]) # 1. 즉시 인쇄
        continue
    # 2. 인쇄중 또는 대기 중인 문서가 있을 때
    standby.append(temp)
    time=temp[1]

'''
연산자 우선 순위를 무시하고 앞에서부터 진행
음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고,그 몫을 음수로 바꾼 것
결과가 최대인 것과 최소인 것

첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다.
(1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데,
차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다.

'''

n = int(input())
array = list(map(int, input().split()))
operator = list(map(int, input().split()))  # +, -, *, //
str_operator = []
for idx, i in enumerate(operator):
    if idx == 0:
        for j in range(i):
            str_operator.append('+')
            continue
    elif idx == 1:
        for j in range(i):
            str_operator.append('-')
            continue
    elif idx == 2:
        for j in range(i):
            str_operator.append('*')
            continue
    elif idx == 3:
        for j in range(i):
            str_operator.append('//')
            continue

answer = set()
operator_len = len(str_operator)
visited = [0 for _ in range(operator_len)]
now = array[0]


def cal(n1, n2, oper):
    if oper == '+':
        return n1 + n2
    elif oper == '-':
        return n1 - n2
    elif oper == '*':
        return n1 * n2
    else:
        if n1 < 0:
            n1 = -n1
            return -(n1 // n2)
        else:
            return n1 // n2


def dfs(depth, now):
    if operator_len == depth:
        # 끝에 다다른 경우
        answer.add(now)
        return
    for i in range(operator_len):
        if visited[i]:  # 이미 방문했을 경우 = 건너뛰기 과정
            continue
        visited[i] = 1
        temp = now
        now = cal(temp, array[depth+1], str_operator[i])
        dfs(depth + 1, now)
        visited[i] = 0
        now = temp


dfs(0, now)
print(max(answer))
print(min(answer))

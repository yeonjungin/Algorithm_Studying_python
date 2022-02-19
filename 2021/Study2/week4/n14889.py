'''
능력치 Sij=> i와 j가 같은 팀일 때 팀에 더해지는 능력치
팀의 능력치 = 느엵치 Sij의 합
Sij!=Sji일수도 있다. 같을 수도 다를 수도
스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다
음.. 백트래킹,,?
'''
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
each = [sum(x) + sum(y) for x, y in zip(arr, zip(*arr))]
total = sum(each) // 2
print(min(abs(total - sum(each[e] for e in c)) for c in combinations(range(1, n), n // 2)))
# n = int(input())
# s = [list(map(int, input().split())) for _ in range(n)]
# answer = 1000000000
# visited = [0] * n
# cnt = 0
#
#
# def func(s_team, t_team):
#     global answer
#     s_sum = 0
#     t_sum = 0
#     for i in range(len(s_team)):
#         for j in range(i + 1, n//2):
#             s_sum += s[s_team[i]][s_team[j]] + s[s_team[j]][s_team[i]]
#             t_sum += s[t_team[i]][t_team[j]] + s[t_team[j]][t_team[i]]
#     answer = min(answer, abs(s_sum - t_sum))
#
#
# def dfs(next, cnt):
#     if cnt == n // 2:
#         s_team = [idx for idx, i in enumerate(visited) if visited[idx] == 1]
#         t_team = [idx for idx, i in enumerate(visited) if visited[idx] == 0]
#         func(s_team, t_team)
#         return
#
#     for i in range(next, n):
#         if visited[i]:  # *****
#             continue
#         visited[i] = 1
#         dfs(i + 1, cnt + 1)
#         visited[i] = 0
#
#
# dfs(0, cnt)
# print(answer)
#

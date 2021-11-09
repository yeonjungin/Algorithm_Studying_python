import sys

n= int(sys.stdin.readline())
dic={}

for _ in range(2 * n - 1):
    person = sys.stdin.readline().rstrip()
    if person not in dic:
        dic[person]=1
    else:
        del dic[person]
print(*dic)
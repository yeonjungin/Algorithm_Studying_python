from collections import deque

n = int(input())
array =deque(enumerate(map(int, input().split())))
answer=[]

while array:
    idx,balloon=array.popleft()
    answer.append(idx+1)
    if balloon>0:
        array.rotate(-(balloon-1))
    else:
        array.rotate(-balloon)
print(*answer)

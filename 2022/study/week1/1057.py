n,Kim,Lim=map(int,input().split())
answer=0
while Kim!=Lim:
    Kim-=Kim//2
    Lim-=Lim//2
    answer+=1
print(answer)
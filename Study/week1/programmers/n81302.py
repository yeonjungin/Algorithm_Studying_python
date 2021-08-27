from collections import deque

D=((-1,0),(1,0),(0,-1),(0,1)) #상,하,좌,우 / 성능개선을 위해 튜플로 정의

def bfs(place,row,col):
    visited=[[False for _ in range(5)] for _ in range(5)]
    queue=deque()
    visited[row][col]=True
    queue.append((row,col,0)) #행,열,좌표
    while queue:
        now=queue.popleft()
        if now[2]>2:
            continue
        if now[2]!=0 and place[now[0]][now[1]]=='P': # 자기 자신(P)가 아닌 다른 P를 만났다.
            return False
        for i in range(4):
            nx=now[0]+D[i][0]
            ny=now[1]+D[i][1]
            if nx<0 or nx>4 or ny<0 or ny>4:
                continue
            if visited[nx][ny]:
                continue
            if place[nx][ny]=='X':
                continue
            visited[nx][ny]=True
            queue.append((nx,ny,now[2]+1))
            
    return True
    

def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j]=='P':
                if bfs(place,i,j)==False:
                    # 거리두기 지키지 x
                    return False
                
    return True
        

def solution(places):
    answer=[]
    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
            
    return answer
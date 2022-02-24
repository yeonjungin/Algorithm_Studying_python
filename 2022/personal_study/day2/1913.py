n = int(input())
input_num = int(input())
dic = {}
array=[[0 for _ in range(n)] for _ in range(n)]
temp = 1  # 1~N까지의 정수 (표에 들어갈)
x, y = n // 2, n // 2
dic[temp] = (x, y)
array[x][y]=1
# 상,우,하,좌
dx = [-1,0,1,0]
dy = [0, 1, 0, -1]
cnt = 1

for i in range(1, n + 1):
    if i==n:
        for j in range(i-1):
            # 상
            temp+=1
            x+=dx[0]
            y+=dy[0]
            dic[temp]=(x,y)
            array[x][y]=temp
        break
    if i % 2 != 0:  # 상, 우
        for j in range(i):
            # 상
            temp += 1
            x += dx[0]
            y += dy[0]
            dic[temp] = (x, y)
            array[x][y]=temp

        for j in range(i):
            # 우
            temp+=1
            x+=dx[1]
            y+=dy[1]
            dic[temp]=(x,y)
            array[x][y]=temp

    else:  # 하,좌
        for j in range(i):
            # 하
            temp+=1
            x+=dx[2]
            y+=dy[2]
            dic[temp]=(x,y)
            array[x][y]=temp

        for j in range(i):
            # 좌
            temp+=1
            x+=dx[3]
            y+=dy[3]
            dic[temp]=(x,y)
            array[x][y]=temp

    cnt += 1

for i in range(n):
    print(*array[i])
print(dic[input_num][0]+1,dic[input_num][1]+1)
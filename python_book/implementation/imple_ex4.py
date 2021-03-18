'''
Chapter4. 구현
실전 3번문제. 게임 개발
많이 풀어봐야 하는 문제 *** 
'''
n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

'''
dx, dy 정하는 방법!
위 같은 경우 방향이 (북->동->남->서)이니까
(-1,0), (0,1), (1,0), (0,-1)으로 나타낼 수 있다.
여기서 dx에는 튜플의 첫 번째 값들을 모아서 차례대로 저장하기
dy 리스트에는 튜플의 두 번째 값에 모아서 차례대로 저장하기
그래서 dx[0],dy[0] -> (-1,0) (북) 
dx,dy라는 별도의 리스트를 만들어 방향을 정하면, 반복문을 이용해서
모든 방향을 차례대로 확인할 수 있다.
'''


# 북,동,남,서 || 0,1,2,3
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1  # 캐릭터가 방문한 칸의 수
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:  # 왼쪽 방향에 가보지 않은 칸이 존재
        d[nx][ny] = 1  # 방문처리
        x = nx # 바라보고 있는 방향으로 한 칸 전진하는 전과정
        y = ny # 바라보고 있는 방향으로 한 칸 전진하는 전과정
        count += 1 # 현재 칸 방문처리
        turn_time = 0
        continue  # 1단계로 돌아가는 과정
    else: #왼쪽 방향에 가보지 않은 칸이 없거나 바다인 경우
        turn_time += 1 #회전만 하고 1단계로 다시 돌아감

    if turn_time == 4: # 네 방향 모두 갈 수 없는 경우
        nx = x - dx[direction] # 바라보는 방향을 유지한채로 한 칸 뒤로가는 전과정
        ny = y - dy[direction] # 바라보는 방향을 유지한채로 한 칸 뒤로가는 전과정
        if array[nx][ny] == 0: # 뒤로 갈 수 있으면 이동
            x = nx #뒤로 갈 수 있으니까 x,y에 입력
            y = ny #뒤로 갈 수 있으니까 x,y에 입력
        else: # 뒤가 바다로 막혀있는 경우
            break #움직임을 멈춘다 while문 break로 걸어버리기
        turn_time = 0 #1단계로 돌아가서 다시 회전해야하니까 0으로 초기화화
print(count)



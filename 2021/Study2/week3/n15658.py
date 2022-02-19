n = int(input())
array = list(map(int, input().split()))
operator = list(map(int, input().split()))
maxResult = -1000000000
minResult = 1000000000


def dfs(idx, temp):
    global maxResult, minResult
    if idx == n-1:  # 연산자를 사이사이에 다 끼워넣었을 경우
        minResult = min(minResult, temp)
        maxResult = max(maxResult, temp)
        return
    if operator[0] > 0:  # +
        operator[0] -= 1
        dfs(idx + 1, temp + array[idx+1])
        operator[0] += 1
    if operator[1] > 0:  # -
        operator[1] -= 1
        dfs(idx + 1, temp - array[idx+1])
        operator[1] += 1
    if operator[2] > 0:  # *
        operator[2] -= 1
        dfs(idx + 1, temp * array[idx+1])
        operator[2] += 1
    if operator[3] > 0:  # //
        operator[3] -= 1
        dfs(idx + 1, int(temp / array[idx+1]))
        operator[3] += 1


dfs(0, array[0])
print(maxResult)
print(minResult,end='')
'''
+ - X // 2 3 1 2 
+ dfs(+ : 1, - : 3, x :1 ,// :2)
    + dfs(+:0, - : 3, x :1 ,// :2)
        - dfs (+:0, - : 2, x :1 ,// :2)
         - dfs (+:0, - : 1, x :1 ,// :2)
          - dfs(+:0, - : 0, x :1 ,// :2)
            * dfs(+:0, - : 1, x :1 ,// :2)
              dfs(+:0, - : 1, x :0 ,// :2)
              * dfs(+:0, - : 3, x :1 ,// :1)
'''

for i in range(int(input())):
    n = int(input())
    dp = [[0 for _ in range(11)] for _ in range(n+1)]
    dp[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
    dp[1] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 55]
    if n == 1:
        print("10")
        continue
    elif n == 2:
        print("55")
        continue
    for i in range(2, n+1):
        for j in range(11):
            if j == 0:
                dp[i][0] = dp[i - 1][10]
            elif j == 10:
                dp[i][j] = sum(dp[i])
            else:
                dp[i][j] = dp[i][j - 1] - dp[i - 1][j - 1]
    print(dp[n-1][10])
'''
    0   1   2   3   4   5   6   7   8   9   10
2   10  9   8   7   6   5   4   3   2   1   55     
3   55  45  36  28  21  15  10  6   3   1   220
4   220 165
5
6
7
8
9
10
11
12
.. 
'''


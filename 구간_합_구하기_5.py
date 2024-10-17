'''
https://www.acmicpc.net/problem/11660
백준 구간 합 구하기 5 (실버1)
'''

n, m = map(int, input().split())
table = [ list(map(int, input().split())) for _ in range(n) ]
# xy = [ list(map(int, input().split())) for _ in range(m) ]

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + table[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    answer = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(answer)
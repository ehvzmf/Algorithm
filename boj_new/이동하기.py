'''
https://www.acmicpc.net/problem/11048
백준 이동하기 (실버2) - DP, top-down
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
candy = [ list(map(int, input().split())) for _ in range(N) ]
dp = [[0] * (M + 1)] * (N + 1)

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + candy[i-1][j-1]

print(dp[N][M])
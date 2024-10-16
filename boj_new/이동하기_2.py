'''
https://www.acmicpc.net/problem/11048
백준 이동하기 (실버2) - DP, bottom-up
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
candy = [ list(map(int, input().split())) for _ in range(N) ]
dp = [[0] * M] * N

dp[0][0] = candy[0][0]

for i in range(N):
    for j in range(M):
        if i + 1 < N and j + 1 < M:
            dp[i+1][j+1] = max(dp[i][j] + candy[i+1][j+1], dp[i+1][j+1])
        if i + 1 < N:
            dp[i+1][j] = max(dp[i][j] + candy[i+1][j], dp[i+1][j])
        if j + 1 < M:
            dp[i][j+1] = max(dp[i][j] + candy[i][j+1], dp[i][j+1])

print(dp[N-1][M-1])

# 틀림. 나중에 다시 확인 필요
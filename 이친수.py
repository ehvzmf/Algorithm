'''
https://www.acmicpc.net/problem/2193
백준 이친수 (실버3) - DP
'''

# 점화식 찾기: dp[i-1] + dp[i-2]

n = int(input())
dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])
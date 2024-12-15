# https://www.acmicpc.net/problem/13699
# 백준 점화식 (실버4) - dp

n = int(input())
dp = [0] * (n + 1)

dp[0] = 1

for i in range(1, n+1):
    for j in range(i):
        dp[i] += dp[j] * dp[i-(j+1)]
        
print(dp[n])
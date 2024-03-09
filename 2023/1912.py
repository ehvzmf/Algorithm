# https://www.acmicpc.net/problem/1912
# 연속합 (백준) - DP

n = int(input())
arr = list(map(int, input().split()))

# arr[i]까지 고려했을 시 최대 연속합
dp = [0] * n
for i in range(1, n):
  dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))

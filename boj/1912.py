'''
https://www.acmicpc.net/problem/1912
백준 1912 - 연속합 (dp)
'''

import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

dp = [0] * n
dp[0] = num[0]
for i in range(1, n):
    dp[i] = max(num[i], dp[i-1]+num[i])
print(max(dp))

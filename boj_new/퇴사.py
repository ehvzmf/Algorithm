'''
https://www.acmicpc.net/problem/14501
백준 퇴사 (실버3) - dp/bruteforce
'''

n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n) ]

dp = [0] * (n + 1)

'''
for i in range(n): # 상담은 i부터 i + arr[i][0]까지
    for j in range(i + arr[i][0], n+1): # 상담이 끝나는 날짜 ~ 마지막 날까지 반복
        if dp[j] < dp[i] + arr[i][1]:
            # 상담을 포함한 최대 수익 반영
            dp[j] = dp[i] + arr[i][1]

print(dp[-1])
'''

# top down
for i in range(n-1, -1, -1):
    if i + arr[i][0] > n: # 퇴사일을 넘길 경우
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], arr[i][1] + dp[i + arr[i][0]])

print(dp[0])
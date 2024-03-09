'''

https://www.acmicpc.net/problem/12852
백준 12852 - 1로 만들기 2

정수 X에 사용할 수 있는 연산은 세 가지: 
 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
 2. X가 2로 나누어 떨어지면, 2로 나눈다.
 3. 1을 뺀다.
정수 N이 주어졌을 때 위 세 개를 적절히 사용해 1을 만들고자 한다. 
INPUT : 첫째 줄 자연수 1 <= N <= 10^6
OUTPUT : 첫째 줄에 연산을 하는 횟수의 최솟값,
         둘째 줄에 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해 순서대로 출력
          (정답이 여러 개면 아무거나 출력)

'''

import sys
input = sys.stdin.readline

n = int(input())
# DP 테이블 (x를 만드는 최소 연산의 수, [방법])
dp = [[0, []] for _ in range(n+1)]
# 초기화
dp[1][0] = 0
dp[1][1] = [1]

for i in range(2, n+1):
      dp[i][0] = dp[i-1][0] + 1
      dp[i][1] = dp[i-1][1] + [i]
      if i % 3 == 0 and dp[i // 3][0] + 1 < dp[i][0]:
            dp[i][0] = dp[i // 3][0] + 1
            dp[i][1] = dp[i // 3][1] + [i]
      if i % 2 == 0 and dp[i // 2][0] + 1 < dp[i][0]:
            dp[i][0] = dp[i // 2][0] + 1
            dp[i][1] = dp[i // 2][1] + [i]

print(dp[n][0])
print(*reversed(dp[n][1]))

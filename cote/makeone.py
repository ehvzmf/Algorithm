import sys

n = int(sys.stdin.readline())

# DP 테이블 (x를 만드는 최소 연산의 수, [x를 최소 연산으로 만드는 방법])
dp = [[0, [] for _ in range(n+1)]

# DP 테이블에 f(1)의 경우를 초기화
dp[1][0] = 0
dp[1][1] = [1]

for x in range(2, n+1):

      # 먼저, f(x-1) + 1를 사용해 DP 테이블 채우기
      dp[x][0] = dp[x-1][0] + 1
      dp[x][1] = dp[x-1][1] + [x]

      # 이후, x가 2로 나눠지는 경우
      if (x % 2 == 0):
          # f(x//2) + 1 와 기존 DP 테이블 값을 비교해 최솟값으로 전환
          if(dp[x][0] > dp[x//2][0] + 1):
              dp[x][0] = dp[x//2][0] + 1
              dp[x][1] = dp[x//2][1] + [x]

      # 이후, x가 3으로 나눠지는 경우
      if (x % 3 == 0):
          # f(//3) + 1 와 기존 DP 테이블의 값을 비교해 최솟값으로 전환
          if(dp[x][0] > dp[x//3][0] + 1):
              dp[x][0] = dp[x//3][0] + 1
              dp[x][1] = dp[x//3][1] + [x]

# x를 만드는 최소 연산의 수
print(dp[n][0])
# x를 최소 연산으로 만드는 방법
for i in dp[n][1][::-1]:
      print(i, end=" ")
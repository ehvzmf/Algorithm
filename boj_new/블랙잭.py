# https://www.acmicpc.net/problem/2798
# 백준 브론즈2, 브루트포스

n, m = map(int, input().split())
card = list(map(int, input().split()))
card.sort(reverse=True)
sum = card[0] + card[1]

for i in range(2, n):
    sum += card[i]

    if sum <= m:
        print(sum)
        break
    else: 
        sum -= card[i-2]
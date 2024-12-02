# https://www.acmicpc.net/problem/10816
# 백준 숫자 카드2 (실버4) - 이분탐색

n = int(input())
card = list(map(int, input().split()))
m = int(input())
goal = list(map(int, input().split()))

answer = [0] * m
count = 0

for i in range(m):
    for j in range(n):
        if goal[i] == card[j]:
            count += 1
    answer[i] = count
    count = 0

print(' '.join(map(str, answer)))
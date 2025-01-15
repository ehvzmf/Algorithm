# https://www.acmicpc.net/problem/1773
# 백준 브론즈2 - 구현, 브루트포스 (9/19)

n, c = map(int, input().split())
time = [0] * c

for _ in range(n):
    p = int(input()) # period
    if p == 1:
        answer = c
    time[p-1::p] = [1] * (c//p)

answer = sum(time)

print(answer)
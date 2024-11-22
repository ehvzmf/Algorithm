# https://www.acmicpc.net/problem/2845
# 브론즈4, 구현

L, P = map(int, input().split())
arr = list(map(int, input().split()))

answer = L * P

for i in range(len(arr)):
    arr[i] -= answer

print(' '.join(map(str, arr)))
# https://www.acmicpc.net/problem/2480
# 백준 브론즈4

num = list(map(int, input().split()))
num.sort()
answer = 0

if num[0] == num[1] and num[1] == num[2]:
    answer = 10000 + num[0] * 1000
elif num[0] == num[1] or num[1] == num[2]:
    answer = 1000 + num[1] * 100
else:
    answer += num[2] * 100

print(answer)
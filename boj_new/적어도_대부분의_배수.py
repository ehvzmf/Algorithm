# https://www.acmicpc.net/problem/1145
# 브론즈1, 브루트포스

num = list(map(int, input().split()))
min = min(num)

while 1:
    count = 0
    for i in num:
        if min % i == 0:
            count += 1
    if count > 2:
        break
    min += 1
print(min)
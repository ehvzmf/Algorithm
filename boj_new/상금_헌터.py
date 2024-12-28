# https://www.acmicpc.net/problem/15953
# 백준 브론즈3 (카카오 코드 페스티벌)

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    ans = 0

    if not a == 0:
        if a == 1:
            ans += 5000000
        elif a <= 3:
            ans += 3000000
        elif a <= 6:
            ans += 2000000
        elif a <= 10:
            ans += 500000
        elif a <= 15:
            ans += 300000
        elif a <= 21:
            ans += 100000

    if not b == 0:
        if b == 1:
            ans += 5120000
        elif b <= 3:
            ans += 2560000
        elif b <= 7:
            ans += 1280000
        elif b <= 15:
            ans += 640000
        elif b <= 31:
            ans += 320000
    
    print(ans)
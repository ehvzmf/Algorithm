'''
https://www.acmicpc.net/problem/10250
백준 ACM 호텔 (브론즈3)
'''
t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    floor = n % h
    room = n // h + 1

    if floor == 0: 
        room -= 1
        floor = h

    print(floor * 100 + room)
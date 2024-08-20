'''
https://www.acmicpc.net/problem/2525
백준 2525 - 오븐 시계 (브론즈3)
'''

H, M = map(int, input().split())
C = int(input())

minute = M + C
H += minute // 60
minute = minute % 60

if H >= 24:
    H -= 24

print(H, minute)

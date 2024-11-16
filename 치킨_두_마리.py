# https://www.acmicpc.net/problem/14489
# 백준 치킨 두 마리 (브론즈4) - 구현

A, B = map(int, input().split())
C = int(input())

if C*2 > (A + B):
    print(A + B)
else:
    print(A + B - C*2)
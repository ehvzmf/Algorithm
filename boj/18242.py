'''
https://www.acmicpc.net/problem/18242
백준 18242 - 네모네모 시력검사 (실4, 구현/애드 혹)
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
S = None
C = 0

for i in range(N):
    a = list(input())
    arr.append(a)
    if '#' in a and not S:
        S = (i, a.index('#'))
        C = a.count('#')

if C % 2 == 0:
    print('UP')
else:
    if arr[S[0] + C//2][S[1]] == '.':
        print('LEFT')
    elif arr[S[0] + C - 1][S[1] + C//2] == '.':
        print('DOWN')
    else:
        print('RIGHT')

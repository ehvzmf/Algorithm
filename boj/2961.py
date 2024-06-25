'''
https://www.acmicpc.net/problem/2961
백준 2961 - 백트레킹
'''

import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
ing = [list(map(int, input().split())) for _ in range(n)] 
result = 1e9

for cmbs in [combinations(ing, i) for i in range(1, n+1)]:
    for c in cmbs:
        sour, bitter = 1, 0 
        for s, b in c:
            sour *= s
            bitter += b
        result = min(result, abs(sour-bitter))
        
print(result)

# https://www.acmicpc.net/problem/11286
# 백준 실버1 - 우선순위 큐

'''
절댓값 힙
1. 배열에 정수 x(x != 0)을 넣는다. 
2. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거
'''

import sys
import heapq

n = int(input())
q = []

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a != 0:
        heapq.heappush(q, (abs(a), a))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
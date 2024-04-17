'''
https://www.acmicpc.net/problem/1927
백준 1927: 최소 힙
'''

import sys
import heapq

n = int(input())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x != 0: 
        heapq.heappush(heap, x)
    else: 
        try:
            print(heapq.heappop(heap))
        except:
            print(0)

'''
https://www.acmicpc.net/problem/2178
백준 2178 : 미로 탐색 (그래프 이론) 
'''
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
queue = deque([(0, 0)])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        next_x, next_y = x + dx[i], y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < m:
            if graph[next_x][next_y] == 1:
                queue.append((next_x, next_y))
                graph[next_x][next_y] = graph[x][y] + 1

print(graph[n-1][m-1])

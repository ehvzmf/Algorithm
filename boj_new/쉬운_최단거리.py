# https://www.acmicpc.net/problem/14940
# 백준 실버1 - bfs

import sys
from collections import deque

n, m = map(int, input().split())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

graph = []
Q = deque()
ch = [[0] * m for _ in range(n)]

for r in range(n):
    graph.append(list(map(int, input().split())))
    
    for c in range(m):
        if graph[r][c] == 2:
            graph[r][c] = 0
            Q.append([r, c])
            ch[r][c] = 1

while Q:
    for _ in range(len(Q)):
        r, c = Q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and ch[nr][nc] == 0 and graph[nr][nc] == 1:
                ch[nr][nc] = 1
                graph[nr][nc] = graph[r][c] + 1
                Q.append([nr, nc])

for i in range(n):
    for j in range(m):
        if ch[i][j] == 0 and graph[i][j] == 1:
            graph[i][j] = -1
    print(*graph[i])
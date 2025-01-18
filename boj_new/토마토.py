# https://www.acmicpc.net/problem/7576
# 백준 골드5 - bfs

import sys
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

m, n = map(int, input().split())
tray = []

for _ in range(n):
    tray.append(list(map(int, input().split())))

Q = deque()

# 토마토 중 익은 토마토 큐에 삽입
for r in range(n):
    for c in range(m):
        if tray[r][c] == 1:
            Q.append([r, c])

while Q:
    for _ in range(len(Q)):
        r, c = Q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
        
            if nr >= 0 and nr < n and nc >= 0 and nc < m and tray[nr][nc] == 0:
                tray[nr][nc] = tray[r][c] + 1

                Q.append([nr, nc])

day = 0

for row in tray:
    for t in row:
        if t == 0:
            print(-1)
            exit(0)
    day = max(day, max(row))
print(day - 1)
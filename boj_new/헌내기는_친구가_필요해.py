# https://www.acmicpc.net/problem/21736
# 백준 실버2 - Graph, dfs, bfs (time limit: 2s)

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
campus = []                         # O - 빈공간, X - 벽, I - 내 위치, P - 다른 사람
start = ()

for i in range(n):
    row = list(input())
    for j in range(m):
        if row[j] == 'I':
            start = (i, j)
    campus.append(row)

# bfs
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[0] * m for _ in range(n)]
answer = 0

queue = deque([start])
visited[start[0]][start[1]] = 1

while(queue):
    x, y = queue.popleft()

    for dx, dy in d:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m:
            if campus[nx][ny] != 'X' and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1

                if campus[nx][ny] == 'P':
                    answer += 1

print(answer if answer > 0 else 'TT')
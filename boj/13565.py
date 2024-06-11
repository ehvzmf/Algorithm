'''
https://www.acmicpc.net/problem/13565
2차 스터디 1주차 (dfs)
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000000)

m, n = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(m)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    graph[x][y] = 2
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if (0<=nx<m) and (0<=ny<n) and graph[nx][ny] == 0:
            dfs(nx, ny)

for i in range(n):
    if graph[0][i] == 0:
        dfs(0, i)

print("YES" if 2 in graph[-1] else "NO")

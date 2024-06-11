'''
https://www.acmicpc.net/problem/1325
2차 스터디 1주차 (bfs)
'''

from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    visited = [0] * (n+1)
    q = deque([i])
    visited[i] = 1
    count = 1

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                q.append(nx)
                visited[nx] = 1
                count += 1
    return count
    
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    
max_hack = 0
answer = []

for i in range(1, n+1):
    result = bfs(i)
    if max_hack < result:
        max_hack = result
        answer = [i]
    elif max_hack == result:
        answer.append(i)

print(*answer)

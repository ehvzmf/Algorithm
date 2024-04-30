'''
https://www.acmicpc.net/problem/24479
백준 24479: 알고리즘 수업 - 깊이 우선 탐색 1 (dfs)
쌩 기초
'''

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

c = 1
def dfs (graph, v, visited):
    global c
    visited[v] = c # 방문하면 순서 나타내기
    
    for i in graph[v]:
        if visited[i] == 0:
            c += 1
            dfs(graph, i, visited) # dfs 재귀

for i in range(m):
    a, b, = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()
    
dfs(graph, r, visited)

for i in range(1, n+1):
    print(visited[i])

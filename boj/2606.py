'''
https://www.acmicpc.net/problem/2606
백준 2606 - 바이러스 (실버3) dfs 풀이
'''

N = int(input())
V = int(input())
graph = [ [] for i in range(N+1) ]
visited = [0] * (N+1)

for i in range(V):
    a, b = map(int, input().split())
    graph[a] += [b] 
    graph[b] += [a]
    
def dfs(V):
    visited[V] = 1
    for nx in graph[V]:
        if visited[nx] == 0:
            dfs(nx)

dfs(1)
print(sum(visited)-1)

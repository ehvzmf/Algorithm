'''
https://www.acmicpc.net/problem/2606
백준 2606 - 바이러스 (실버3) bfs 풀이
'''
from collections import deque

N = int(input())
V = int(input()) # 컴퓨터 쌍의 수
graph = [[] for i in range(N+1)] # 그래프 초기화
visited = [0] * (N+1)

for i in range(V):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

visited[1] = 1 # 1번 컴퓨터부터 시작이니 방문 표시
queue = deque([1])

while queue:
    C = queue.popleft()
    for nx in graph[C]:
        if visited[nx] == 0:
            queue.append(nx)
            visited[nx] = 1
            
print(sum(visited)-1)

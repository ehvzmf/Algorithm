'''
https://www.acmicpc.net/problem/1388
백준 1388 바닥 장식(DFS)
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))
answer = 0

def dfs(row, col):
    if graph[row][col] == "-":
        graph[row][col] = 1
        for a in [1, -1]: # 같은 행 확인
            Y = col + a
            if 0<Y<M and graph[row][Y] == "-":
                dfs(row, Y)
            
    if graph[row][col] == "|":
        graph[row][col] = 1
        for b in [1, -1]: #같은 열 확인
            X = row + b
            if 0<X<N and graph[X][col] == "|": # 다음 노드 같으면 재귀
                dfs(X, col)
            
            
for i in range(N):
    for j in range(M):
        if graph[i][j] == '-' or graph[i][j] == '|':
            dfs(i, j)
            answer += 1
            
print(answer)

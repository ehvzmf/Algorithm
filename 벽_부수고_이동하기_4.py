'''
https://www.acmicpc.net/problem/16946
백준 벽 부수고 이동하기4 (골드2) - dfs/bfs
'''
from collections import deque

def bfs(start)
n, m = map(int, input().split())
graph = [input() for _ in range(n)]
answer = []
temp = ''

for i in range(n):
    for j in graph[i]:
        if j == '0':
            temp += '0'
        else: 

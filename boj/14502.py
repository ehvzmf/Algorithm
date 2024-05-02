'''
https://www.acmicpc.net/problem/14502
4조 스터디 4주차 실전 문제 (dfs)
'''

import sys
input = sys.stdin.readline
from collections import deque
import copy

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0

def bfs():
    queue = deque()
    temp_graph = copy.deepcopy(lab)
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 2:
                queue.append((i,j))
                
    while queue: 
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2
                queue.append((nx, ny))
                
    global answer
    count = 0
    
    for i in range(n):
        count += temp_graph[i].count(0)
    
    answer = max(answer, count)
    
def makeWall(count):
    if count == 3:
        bfs()
        return 
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0: 
                lab[i][j] = 1
                makeWall(count + 1)
                lab[i][j] = 0

makeWall(0)
print(answer)

'''
https://www.acmicpc.net/problem/1189
백준 1189 - 컴백홈 (백트레킹)
'''

import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input().strip()))

move = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# 처음 위치 설정
graph[R-1][0] = 1
result = 0

def dfs(row, col):
    global result
    
    # 집 도착 
    if row == 0 and col == C-1:
        if graph[row][col] == K:
            result += 1
            return
        else:
            return
    
    for i in move:
        x = row + i[0]
        y = col + i[1]
        if x >= 0 and y >= 0 and x < R and y < C:
            if graph[x][y] == '.':
                graph[x][y] = graph[row][col] + 1
                dfs(x, y)
                
                # 다음 케이스를 위해
                graph[x][y] = '.'
    
dfs(R-1, 0)
print(result)

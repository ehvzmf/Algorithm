'''
https://www.acmicpc.net/problem/2580
백준 2580 - 스도쿠 (백트레킹, 18회 기출) 
'''

import sys

def checkRow(x, n):            # x 세로줄의 n이 있는지 확인
    for i in range(9):
        if n == graph[x][i]:
            return False
    return True

def checkCol(y, n):            # y 가로줄의 n이 있는지 확인
    for i in range(9):
        if n == graph[i][y]:
            return False
    return True

def checkRect(x, y, n):        # x, y 좌표가 포함되어 있는 3x3 크기의 사각형의 n이 있는지 확인
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if n == graph[nx+i][ny+j]:
                return False
    return True

def solution(n):                # dfs + 백트래킹
    if n == len(blank):         # 스도쿠의 빈 칸을 채웠다면
        for _ in range(9):
            print(*graph[_])
        exit(0)

    for i in range(1, 10):      # 반복문을 통해 빈칸에 1부터 9까지 넣어본다.
        x = blank[n][0]         # 빈칸의 x좌표
        y = blank[n][1]         # 빈칸의 y좌표
        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            solution(n + 1)
            graph[x][y] = 0

graph = []
blank = []
for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(9):
        if graph[i][j] == 0:
            blank.append([i, j])
solution(0)

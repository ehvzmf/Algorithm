'''
https://www.acmicpc.net/problem/14503
백준 14503 : 로봇 청소기

로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램
방 크기 N x M의 직사각형, 각 칸은 벽 또는 빈 칸. 청소기는 바라보는 방향이 있으며 이 방향은 동, 서, 남, 북 중 하나. 
방의 각 칸은 (r, c)로 나타낼 수 있고 가장 북쪽 줄의 가장 서쪽 칸이 (0,0), 가장 남쪽 줄의 가장 동쪽 칸이 (N-1, M-1)
처음 빈 칸은 전부 청소되지 않은 상태
로봇 청소기 작동: 1. 청소되지 않았으면 현재 칸 청소
                2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
                   1. 바라보는 방향 유지, 후진되면 후진하고 1번으로
                   2. 바라보는 방향의 뒤쪽 칸이 벽이면 작동 멈추기
                3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있으면
                   1. 반시계 방향으로 90도 회전
                   2. 바라보는 방향 기준 앞쪽이 청소되지 않은 빈 칸이면 전진
                   3. 1번으로
INPUT : 첫째 줄에 방 크기 N, M (3<=N, M<=50) / 둘째 줄에 로봇 청소기 좌표 (r,c)와 처음 로봇 청소기가 바라보는 방향 d
        (d = (0 = 북쪽, 1 = 동쪽, 2 = 남쪽, 3 = 서쪽)
        셋째 줄부터 N개의 줄로 각 장소의 상태를 나타내는 N x M 값이 한 줄에 M개씩 출력
        (i,j) = 0이면 청소되지 않은 빈칸, 1이면 벽. 최북/남/서/동쪽은 벽. 로봇 청소기가 있는 칸은 항상 빈 칸
OUTPUT : 작동하는 동안 청소하는 칸의 개수
'''

import sys

def dfs(x, y, v):
    global answer

    # 빈 곳이면 청소
    if graph[x][y] == 0:
        graph[x][y] = 2 # 방문 처리
        answer += 1 # 청소 구역 카운트

    # 반복문을 통해 4방향 확인
    for _ in range(4):
        nv = (v + 3) % 4 # 현재 방향 + 3을 4로 나눈 나머지가 왼쪽 방향
        nx = x + dx[nv]
        ny = y + dy[nv]

        # 이동 위치가 빈 곳이면 탐색
        if graph[nx][ny] == 0:
            dfs(nx, ny, nv)
            return
        # 현재 방향 변경
        v = nv

    # 4방향 모두 탐색
    nv = (v + 2) % 4 # 현재방향 + 2를 4로 나눈 나머지가 후진 방향
    nx = x + dx[nv]
    ny = y + dy[nv]
  
    if graph[nx][ny] == 1:
        return

    # 이동 위치가 벽이 아니라면 탐색
    dfs(nx, ny, v)
  
n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# d => 0,3,2,1 순서로 돌아야함. 북/서/남/동

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0
dfs(r, c, d)
print(answer)

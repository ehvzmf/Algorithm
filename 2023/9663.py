'''
https://www.acmicpc.net/problem/9663
백준 9663 : N-Queen

크기가 N x N인 체스판 위 퀸 N개를 서로 공격할 수 없게 놓는 문제
INPUT : 크기 N (1 <= N <= 15)
OUTPUT : 퀸을 놓는 방법의 수
'''
# 알고리즘은 이렇게 됨. 하지만 시간초과 
'''
n = int(input())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)
'''

# pypy로 풀기. 

import sys
input = sys.stdin.readline

def check(x):
    for i in range(x):
        if rows[x] == rows[i] or abs(rows[x] - rows[i]) == x - i:
            return False
    return True

def dfs(x):
    global cnt

    if x == n:
        cnt += 1
        return

    for i in range(n):
        if visited[i]: 
            continue

        rows[x] = i
        if check(x):
            visited[i] = True
            dfs(x+1)
            visited[i] = False

n = int(input())
rows = [0] * n
visited = [False] * n
cnt = 0

dfs(0)
print(cnt)

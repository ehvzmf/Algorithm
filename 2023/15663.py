'''
https://www.acmicpc.net/problem/15663
백준 15663 - N과 M (9) (백트레킹)
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

visited = [False] * n
tmp = []

def dfs():
    if len(tmp) == m:
        print(*tmp)
        return
    prev = 0
    for i in range(n):
        if not visited[i] and prev != num[i]:
            visited[i] = True
            tmp.append(num[i])
            prev = num[i]
            dfs()
            visited[i] = False
            tmp.pop()
dfs()

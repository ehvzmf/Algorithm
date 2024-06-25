'''
https://www.acmicpc.net/problem/2529
백준 2529 - 부등호 (백트레킹)
'''

import sys
input = sys.stdin.readline

k = int(input())
arr = list(input().split())

visited = [0] * 10
max_answer = ""
min_answer = ""

def check(i, j, k):
    if k == "<":
        return i < j
    else: 
        return i > j

def solve(depth, s):
    global max_answer, min_answer
    
    if(depth == k+1):
        if len(min_answer) == 0:
            min_answer = s
        else:
            max_answer = s
        return
    
    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(s[-1], str(i), arr[depth-1]):
                visited[i] = True
                solve(depth+1, s+str(i))
                visited[i] = False

solve(0, "")
print(max_answer)
print(min_answer)

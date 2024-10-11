'''
https://www.acmicpc.net/problem/14888
백준 14888 - 연산자 끼워넣기 (실버1) - 브루트포스, 백트레킹
'''

N = int(input())
A = list(map(int, input().split()))
oper = list(map(int, input().split()))

mx = -1e9
mn = 1e9

def dfs(n, temp):
    global mx, mn

    # 종료 조건
    if n == N-1:
        mx = max(temp, mx)
        mn = min(temp, mn)
        return
    
    if oper[0] != 0:
        oper[0] -= 1
        dfs(n+1, temp + A[n+1])
        oper[0] += 1

    if oper[1] != 0:
        oper[1] -= 1
        dfs(n+1, temp - A[n+1])
        oper[1] += 1

    if oper[2] != 0:
        oper[2] -= 1
        dfs(n+1, temp * A[n+1])
        oper[2] += 1

    if oper[3] != 0:
        oper[3] -= 1
        # 음수의 나눗셈 주의
        dfs(n+1, int(temp / A[n+1]))
        oper[3] += 1

dfs(0, A[0])

print(mx)
print(mn)
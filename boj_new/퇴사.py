'''
https://www.acmicpc.net/problem/14501
백준 퇴사 (실버3) - dp/bruteforce
'''

n = int(input())
T = [0] * n
P = [0] * n
for i in range(n):
    T[i], P[i] = map(int, input().split())

print(T)
print(P)
'''
https://www.acmicpc.net/problem/11047
백준 동전0 (실버4) - 그리디
'''

n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]
count = 0 

# for i in reversed(A):
for i in range(n-1, -1, -1):
    count += k // A[i]
    k %= A[i]

print(count)
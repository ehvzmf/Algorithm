'''
https://www.acmicpc.net/problem/2439
백준 2439 - 별 찍기2 (브4)
'''

n = int(input())
for i in range(1, n+1):
    print(" " * (n-i) + "*" * i)

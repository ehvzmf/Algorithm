'''
https://www.acmicpc.net/problem/2749
백준 2749 - 피보나치 수 3 (dp)
'''

n = int(input())
a, b = 0, 1
n = n % (15 * (10**5))
for i in range(n):
    a, b = b % (10**6), (a+b) % (10**6)
print(a)

'''
https://www.acmicpc.net/problem/2749
백준 2749 - 피보나치 수 3 (dp)
'''

n = int(input())

mod = 1000000
fibo = [0, 1]
p = mod//10*15

for i in range(2, p):
    fibo.append(fibo[i-1] + fibo[i-2])
    fibo[i] %= mod

print(fibo[n%p])

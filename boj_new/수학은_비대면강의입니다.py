# https://www.acmicpc.net/problem/19532
# 백준 브론즈2, 브루트포스

'''
ax + by = c
dx + ey = f
x = (c - by)/a = (f - ey)/d
y = (c - ax)/b = (f - dx)/e
'''

a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if a*i + b*j == c and d*i + e*j == f:
            print(i, j)

'''
시간 단축:
x = int((c*e-b*f)/(a*e-b*d))
y = int((c*d-a*f)/(b*d-a*e))
'''
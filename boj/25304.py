'''
https://www.acmicpc.net/problem/25304
백준 25304 - 영수증 (브4)
'''

X = int(input())
N = int(input())
sum = 0

for _ in range(N):
    price, count = map(int, input().split())
    sum += (price*count)

if X == sum: 
    print("Yes")
else: 
    print("No")

'''
https://www.acmicpc.net/problem/14719
백준 빗물 (골드5) - 전에 풀었음
'''

H, W = map(int, input().split())
block = list(map(int, input().split()))
answer = 0

for i in range(1, W-1):
    left = max(block[:i])
    right = max(block[i+1:])
    compare = min(left, right)

    if block[i] < compare: 
        answer += compare - block[i]

print(answer)
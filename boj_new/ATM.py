'''
https://www.acmicpc.net/problem/11399
백준 ATM (실버4) - 그리디
'''

n = int(input())
arr = list(map(int, input().split()))
answer = 0
arr.sort()

for i in range(n):
    answer += arr[i] * (n-i)

print(answer)
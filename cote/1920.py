'''
백준 1920 - 수 찾기 (이분탐색)
'''
import sys

n = int(input())
num = list(map(int, sys.stdin.readline().split()))
num.sort()

m = int(input())
mum = list(map(int, sys.stdin.readline().split()))

def binary(target):
    global start, end
    while start <= end:
        mid = (start + end) // 2
        if num[mid] == target:
            return True
    
        if target < num[mid]:
            end = mid - 1
        else:
            start = mid + 1

for i in range(m):
    start = 0
    end = n - 1
    if binary(mum[i]):
        print(1)
    else:
        print(0)

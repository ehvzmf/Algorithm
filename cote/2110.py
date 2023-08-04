'''
https://www.acmicpc.net/problem/2110
백준 2110 - 공유기 설치
'''
import sys
input = sys.stdin.readline

# n, c = map(int, input().split())
# n, c = list(map(int, input().split()))
n, c = list(map(int, input().split(' ')))
array = []

for _ in range(n):
    array.append(int(input()))
array = sorted(array)

start = 1 # min gap
end = array[-1] - array[0] # max gap
result = 0

while(start <= end):
    mid = (start + end) // 2 # mid == gap
    current = array[0]
    count = 1
    for i in range(1, len(array)):
        if array[i] >= current + mid:
            count += 1
            current = array[i]

    if count >= c:  # c 이상의 공유기 설치 가능
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)

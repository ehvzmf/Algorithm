# https://www.acmicpc.net/problem/31669
# 백준 브론즈3 - 구현

N, M = map(int, input().split())
schedule = [input() for _ in range(N)]
zipList = list(map(list, zip(*schedule)))

result = 0
for i in range(len(zipList)):
    if zipList[i].count("X") == N:
        result = i + 1
        break

if result > 0:
    print(result)
else:
    print("ESCAPE FAILED")
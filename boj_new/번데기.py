# https://www.acmicpc.net/problem/15721
# 백준 실버5 - 브루트포스, 시뮬레이션

A = int(input()) # 게임 진행하는 사람 A명
T = int(input()) # 구하고자 하는 번째 T
sign = int(input()) # 뻔 = 0, 데기 = 1 (예외처리도 해야 할까?)

pattern = [0, 1, 0, 1, 0, 0, 1, 1]

for i in range(2, 5001):
    pattern += [0, 1, 0, 1]
    pattern += [0] * (i+1)
    pattern += [1] * (i+1)

current = [0, 0]

for i, j in enumerate(pattern):
    current[j] += 1

    if current[sign] == T:
        print(i % A)
        break
# https://www.acmicpc.net/problem/5596
# 백준 시험 점수 (브론즈4)

mg = list(map(int, input().split()))
ms = list(map(int, input().split()))

if sum(ms) > sum(mg):
    print(sum(ms))
else:
    print(sum(mg))
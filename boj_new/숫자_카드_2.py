# https://www.acmicpc.net/problem/10816
# 백준 숫자 카드2 (실버4) - 이분탐색

from collections import Counter

n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
goal = list(map(int, input().split()))

counter = Counter(card)

for i in goal:
    print(counter[i], end=' ')
# https://www.acmicpc.net/problem/7795
# 백준 실버3, 이분탐색/투 포인터

import bisect

def bin_search(li, a):
    s, e = 0, len(li) - 1
    res = -1
    while s <= e:
        m = (s + e) // 2
        if li[m] < a:
            res = m
            s = m + 1
        else:
            e = m - 1
    return res

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    answer = 0

    for a in A:
        answer += (bisect.bisect(B, a-1))
    
    print(answer)
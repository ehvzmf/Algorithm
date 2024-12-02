# https://www.acmicpc.net/problem/10816
# 백준 숫자 카드2 (실버4) - 이분탐색

n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
goal = list(map(int, input().split()))

dic = {}
for c in card:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1

def binary(m, card, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if m == card[mid]:
        return dic[m]
    elif m < card[mid]:
        return binary(m, card, start, mid-1)
    else:
        return binary(m, card, mid+1, end)

for m in goal:
    print(binary(m, card, 0, n-1), end=' ')

'''
이분 탐색 없이 dict만 사용:
for m in goal:
  if m in dic:
    print(dic[m], end=' ')
  else:
     print(0, end=' ')
'''
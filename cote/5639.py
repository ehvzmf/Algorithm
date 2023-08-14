'''
https://www.acmicpc.net/problem/5639
백준 5639 - 이진 검색 트리 (트리, 재귀)
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
num = []

while True:
    try:
        num.append(int(input()))
    except:
        break

def postorder(s, e):    #start-end
    if s > e:
        return
    mid = e + 1
    
    for i in range(s+1, e+1):
        if num[s] < num[i]:
            mid = i
            break
    postorder(s+1, mid-1)
    postorder(mid, e)
    print(num[s])
    
postorder(0, len(num)-1)

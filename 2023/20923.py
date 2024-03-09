'''
https://www.acmicpc.net/problem/20923
백준 20923 - 숫자 할리갈리 게임 (구현, 덱 - 21회 기출)
'''

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
dDeck, sDeck = deque(), deque()
dGround, sGround = deque(), deque()

for i in range(n):
    a, b = map(int, input().split())
    dDeck.appendleft(a)
    sDeck.appendleft(b)

check = True
# 도도와 수연이 카드 내는 총합 = m

while True:
    if check:   # 도도 차례
        dCard = dDeck.popleft()
        dGround.appendleft(dCard)
        check = False
    else:       # 수연 차례 
        sCard = sDeck.popleft()
        sGround.appendleft(sCard)
        check = True
    if not dDeck or not sDeck:
        break
    
    # 도도가 이길 경우우
    if (not check and dCard == 5) or (check and sCard == 5):
        while sGround:  # 더미 합치기
            dDeck.append(sGround.pop())
        while dGround:
            dDeck.append(dGround.pop())

    # 수연이가 이길 경우
    if sGround and dGround and (sGround[0] + dGround[0]) == 5:
        while dGround:
            sDeck.append(dGround.pop())
        while sGround:
            sDeck.append(sGround.pop())
    m -= 1
    if m == 0: break

s, d = len(sDeck), len(dDeck)    
if s == d:
    print('dosu')
elif s < d:
    print('do')
else: print('su')

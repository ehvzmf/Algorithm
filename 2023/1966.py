'''
https://www.acmicpc.net/problem/1966
백준 1966 - 프린터 큐 (구현, deque)
'''

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0
    
    while queue:
        mx = max(queue) # 최댓값 저장
        front = queue.popleft() # front에서 하나 뽑아서
        m -= 1 # 위치가 앞으로 당겨짐
        
        if mx == front:
            count += 1  # m보다 중요도가 큰 것 배출
            if m < 0:   # m이 mx인 경우 (중요도가 같은 경우는?)
                print(count)
                break
            
        else:
            queue.append(front)
            if m < 0:
                m = len(queue) - 1  # 맨 뒤로 이동

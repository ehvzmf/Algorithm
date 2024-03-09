'''
https://www.acmicpc.net/problem/10845
백준 10845 큐 
'''

import sys
input = sys.stdin.readline

N = int(input())
queue = []

for i in range(N):
    inst = input().split()
    
    if inst[0] == "push":
        queue.append(inst[1])
    elif inst[0] == "pop":
        if queue: print(queue.pop(0))
        else: print(-1)
    elif inst[0] == "size":
        print(len(queue))
    elif inst[0] == "empty":
        if len(queue) == 0: print(1)
        else: print(0)
    elif inst[0] == "front":
        if len(queue) == 0:
            print(-1)
        else: print(queue[0])
    elif inst[0] == "back":
        if len(queue) == 0: print(-1)
        else: print(queue[-1])

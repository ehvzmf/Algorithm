'''
https://www.acmicpc.net/problem/1662
백준 1662 - 압축 (스택, 재귀)
'''

import sys
input = sys.stdin.readline

s = input().strip()

def sol():
    stack = []
    count = 0
    before = ''
	
    for i in s:
        if i == '(':
            stack.append([count-1, before])
            count = 0
        elif i == ')':
	        info = stack.pop()
	        count = count * info[1] + info[0]
        else:
            count += 1
            before = int(i)
	        
    print(count)
    
sol()

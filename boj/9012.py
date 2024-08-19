'''
https://www.acmicpc.net/problem/9012
백준 9012 - 괄호 (실버4)
VPS 여부 판별
'''

n = int(input())

for i in range(n):
    stack = []
    temp = input()
    for j in temp:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else: 
            print("NO")

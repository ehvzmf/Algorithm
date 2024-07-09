'''
https://www.acmicpc.net/problem/11899
백준 11899 - 괄호 끼워넣기 (스택)
'''

s = list(input())
stack = []
unmatched_r = 0

for char in s:
    if char == '(':
        stack.append(char)
    elif char == ')' and stack:
        stack.pop()
    else:
        unmatched_r += 1

unmatched_l = len(stack)
print(unmatched_l + unmatched_r)

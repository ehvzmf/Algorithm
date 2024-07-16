'''
https://www.acmicpc.net/problem/1141
백준 1141 - 접두사 (dfs) 
'''

import sys
input = sys.stdin.readline

n = int(input())
word = [input().rstrip() for _ in range(n)]

word.sort(key=len)
answer = 0

for i in range(n):
    flag = False
    
    for j in range(i+1, n):
        if word[i] == word[j][0:len(word[i])]:
            flag = True
            break
        
    if not flag:
        answer += 1

print(answer)

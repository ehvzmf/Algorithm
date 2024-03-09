'''
https://www.acmicpc.net/problem/10808
백준 알파벳개수
'''

s = input()

ap = 97 #alphabet
result = [0] * 26

for j in range(26):
    for i in range(len(s)):
        if s[i] == chr(ap):
            result[j] += 1
    ap += 1
            
for i in range(26):
    print(result[i], end=" ")

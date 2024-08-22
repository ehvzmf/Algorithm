'''
https://www.acmicpc.net/problem/28074
백준 28074 - 모비스 (브4, 구현/문자열)
'''

MOBIS = [ 'M', 'O', 'B', 'I', 'S' ]
word = input()
result = True

for i in MOBIS:
    if i not in word:
        result = False
        break
    
if result:
    print('YES')
else: 
    print('NO')

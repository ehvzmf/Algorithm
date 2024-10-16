'''
https://www.acmicpc.net/problem/10809
백준 알파벳 찾기 - 브론즈2
'''

s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for a in alphabet:
    if a in s:
        # find() 사용해도 ok
        print(s.index(a), end=" ")
    else: 
        print(-1, end=" ")
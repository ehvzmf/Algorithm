'''
https://www.acmicpc.net/problem/5622
백준 다이얼 (브론즈2) 
'''

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
string = input()
time = 0

for s in string:
    for i in dial: 
        if s in i:
            time += dial.index(i) + 3

print(time)
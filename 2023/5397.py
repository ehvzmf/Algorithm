'''
https://www.acmicpc.net/problem/5397
백준 5397 - 키 로거 (키보드를 누른 명령 모두 기록) 

입력한 키가 주어졌을 때 비밀번호를 알아내는 프로그램
알파벳 대소문자/숫자/백스페이스/화살표

INPUT : 테스트 케이스 개수 (한줄, 길이 L인 문자열)
OUTPUT : 각 테스트 케이스에 대한 비밀번호 출력
'''

import sys

n = int(input())

for _ in range(n):
    left = []
    right = []
    
    pwd = list(sys.stdin.readline().rstrip())
    
    for char in pwd:
        if char == ">": 
            if right: left.append(right.pop())
        elif char == "<":
            if left: right.append(left.pop())
        elif char == "-":
            if left: left.pop()
        else: 
            left.append(char)

    print("".join(left)+ "".join(reversed(right)))

'''

https://www.acmicpc.net/problem/1316
백준 1316 - 그룹 단어 체커
: 단어에 존재하는 모든 문자에 대해, 각 문자가 연속해서 나타나면 그룹단어
INPUT : 첫째 줄에 단어의 개수 N (<=100), 둘째 줄부터 N개의줄의 단어 (소문자만, 중복X, 최대 100)
OUTPUT : 그룹 단어의 개수

'''
N = int(input())
count = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            count -= 1
            break

print(count)

'''
https://www.acmicpc.net/problem/25305
백준 25305 - 커트라인 (브3)
'''

N, k = map(int, input().split())
score = list(map(int, input().split()))
score.sort(reverse=True)

print(score[k-1])

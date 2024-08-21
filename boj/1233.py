'''
https://www.acmicpc.net/problem/1233
백준 주사위 - 구현/브루트포스 (브2)
'''

S1, S2, S3 = map(int, input().split())
preq = [0] * 81

for i in range(1, S1+1):
    for j in range(1, S2+1):
        for k in range(1, S3+1):
            preq[i+j+k] += 1
            
print(preq.index(max(preq)))

'''
https://www.acmicpc.net/problem/1043
백준 1043 : 거짓말

과장 섞인 거짓말을 말하고 싶지만 거짓말쟁이로 알려지는 일을 피하기 위해 진실을 아는 사람이 올 경우 진실을 이야기하기.
INPUT : 1. 사람 수 N, 파티 수 M
        2. 이야기의 진실을 아는 사람의 수 / 그 개수만큼 번호 (1~N) (번호로 사람을 구분)
        3. 파티마다 오는 사람 수 / 번호를 1~M
        N, M은 50 이하 자연수
OUTPUT : 거짓말쟁이로 알려지지 않으면서 과장된 이야기를 할 수 있는 파티 개수의 최댓값
'''

import sys
input = sys.stdin.readline

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b, know_truth):
    a = find(parent, a)
    b = find(parent, b)
    
    if a in know_truth and b in know_truth:
        return
    if a in know_truth:
        parent[b] = a
    elif b in know_truth:
        parent[a] = b
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        
n, m = map(int, input().split())
know_truth = list(map(int, input().split()))[1:]

parties = []
parent = list(range(n+1))
answer = 0

for _ in range(m):
    party = list(map(int, input().split()))[1:]
    for i in range(len(party) - 1):
        union(parent, party[i], party[i+1], know_truth)
    parties.append(party)

for party in parties:
    for i in range(len(party)):
        if find(parent, party[i]) in know_truth:
            break
    else:
        answer += 1

print(answer)

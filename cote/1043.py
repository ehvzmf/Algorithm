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

N, M = list(map(int, sys.stdin.readline().split()))
# int(input())
truth = list(map(int, sys.stdin.readline().split()))[1:]

KNOW_TRUTH = 0
# 유니온 파인드용 부모 리스트. 여기서 0번은 사람으로 사용하지 않고, 진실을 아는 사람으로 친다.
parent = [i for i in range(n + 1)]
for person in truth:
    parent[person] = KNOW_TRUTH

# union find 를 하는 이유는 서로 겹치지 않는 그룹 (거짓말을 모르는 그룹과 거짓말을 아는 그룹)으로 나누기 위해서다.
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b 

parties = []
for _ in range(m):
    party = list(map(int, sys.stdin.readline().split()))[1:]
    # 파티의 참석한 사람들에 대해 2명씩 union 해본다.
    for i in range(len(party) - 1):
        union(party[i], party[i + 1])
    parties.append(party)

answer = 0

for party in parties:
    know = False
    for i in range(len(party)):
        # 진실을 알고 있던 그룹에 속했었을 경우
        if find(party[i]) == KNOW_TRUTH:
            know = True
            break
    if not know:
        answer += 1

print(answer)

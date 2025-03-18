# https://www.acmicpc.net/problem/7795
# 백준 실버3, 이분탐색/투 포인터

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    answer = 0

    for i in range(n):
        for j in range(m):
            if A[i] > B[j]:
                answer += 1
    
    print(answer)
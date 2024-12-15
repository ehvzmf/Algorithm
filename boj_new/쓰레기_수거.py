# https://www.acmicpc.net/problem/1680
# 쓰레기 수거 (실버3) - 구현, 시뮬레이션

t = int(input())

for _ in range(t):
    # 쓰레기차의 용량 W, 지점의 개수 N
    w, n = map(int, input().split())
    xw = [list(map(int, input().split())) for _ in range(n)]
    dist = 0
    trash = 0
    prev = 0

    for i in range(n):
        x_i, w_i = xw[i]

        # 전진
        if trash + w_i < w:
            dist += x_i - prev
            trash += w_i
        
        # 용량 도달
        elif trash + w_i == w:
            dist += (x_i - prev) + x_i * 2
            trash = 0
            if i == n-1:
                dist -= x_i * 2
        
        # 용량 초과
        elif trash + w_i > w:
            trash = w_i
            dist += (x_i - prev) + x_i * 2
        prev = x_i

        if i == n-1:
            dist += x_i

    print(dist)
# https://www.acmicpc.net/problem/1680
# 쓰레기 수거 (실버3) - 구현, 시뮬레이션

# 가까운 데부터 쓰레기 모으다가 조건에 해당할 시 쓰레기장 감
# 쓰레기 양이 용량 도달 / 그 지점의 쓰레기를 실을 시 용량 초과 / 더 이상 쓰레기 실을 지점이 없을 때


t = int(input())

for i in range(t):
    # 테케의 첫 번째 쓰레기차의 용량 W, 지점의 개수 N
    w, n = map(int, input().split())

    # N개의 줄에 i번째 지점의 쓰레기장으로부터 거리 x_i, 쓰레기의 양 w_i
    # 각 지점의 x_i는 서로 다르며, x_i가 작은 지점부터 순서대로 입력이 주어진다. 
    xw = [list(map(int, input().split())) for _ in range(n)]

    dist = 0
    trash = 0

    for j in range(n):
        if trash == w or trash + xw[j][1] > w:
            dist += dist*2
            trash = 0
        
        dist += xw[j][0]
        trash += xw[j][1]
        print(j, dist, trash)

    print(dist)
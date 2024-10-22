'''
https://www.acmicpc.net/problem/1051
백준 숫자 정사각형 
'''

def find_square(s):
    for i in range(n - s + 1): # 행
        for j in range(m - s + 1): # 열
            if graph[i][j] == graph[i][j+s-1] == graph[i+s-1][j] == graph[i+s-1][j+s-1]:
                return True
    return False

n, m = map(int, input().split())

# 띄어쓰기 없는 배열 입력 받기
graph = [list(map(int, list(input()))) for _ in range(n)]
size = min(n, m)

# for i in range(start, stop, step)
# 최대 크기부터 하나씩 줄여가면서 시작
for k in range(size, 0, -1):
    if find_square(k):
        print(k**2) # 제곱
        break
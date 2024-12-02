# https://www.acmicpc.net/problem/21921
# 실버3 - 누적합/슬라이딩 윈도우

n, x = map(int, input().split())
arr = list(map(int, input().split()))
summation = [0] * n

for i in range(n):
    for j in range(x):
        summation[i] += arr[i+j]

if max(summation) == 0:
    print('SAD')
else:
    print(max(summation))
    # 어떻게 세지? 
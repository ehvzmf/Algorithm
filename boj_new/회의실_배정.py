'''
https://www.acmicpc.net/problem/1931
백준 회의실 배정 (실버1) - 그리디
'''
n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
end = 0
answer = 0

# 끝나는 시간에 따라 sort
meetings.sort(key=lambda x: (x[1], x[0]))

for a, b in meetings:
    if end <= a: # 이전 회의 시간 <= 다음 회의 시간
        answer += 1 
        end = b

print(answer)
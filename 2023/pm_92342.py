'''
https://school.programmers.co.kr/learn/courses/30/lessons/92342
프로그래머스 92342. 양궁대회 (DFS, 완전탐색, 트리)
INPUT : 화살의 개수 n, 어피치가 맞힌 과녁 점수의 개수 10점부터 0점까지 순서대로 info[10]
OUTPUT : 라이언이 가장 큰 점수 차이로 우승하기 위해 n발의 화살을 어떤 과녘 점수에 맞혀야 하는지 
'''

def solution(n, info):
    max = [-1] * 12
    for win in range(1 << 10):
        # 10-1 점수별 화살 개수, 0점 개수, 점수차이
        cur = [0] * 10 + [n, 0]
        for i in range(10): 
            if win & (1 << i):
                cur[-1] += 10 - i
                cur[-2] -= info[i] + 1
                cur[i] = info[i] + 1
            elif info[i] != 0:     # 어피치 점수 획득
                cur[-1] -= 10 - i
        # 라이언이 지거나 화살을 n발 초과로 쏜 경우
        if cur[-1] <= 0 or cur[-2] < 0:
            continue
            
        if cur[::-1] > max[::-1]:
            max = cur
    if max[-1] <= 0:
        answer = [-1]
    else: answer = max[:-1]
    return answer

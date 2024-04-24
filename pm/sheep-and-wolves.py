'''
https://school.programmers.co.kr/learn/courses/30/lessons/92343
4조 스터디 3주차 실전 문제 - 양과 늑대 (그래프) 
'''

def solution(info, edges):
    visit = [0] * len(info)
    answer = []
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        
        for p, c in edges:
            if visit[p] and not visit[c]:
                visit[c] = 1
                if info[c] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visit[c] = 0
    visit[0] = 1
    dfs(1, 0)
    
    return max(answer)

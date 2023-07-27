'''
https://school.programmers.co.kr/learn/courses/30/lessons/42862
프로그래머스 42862. 체육복 (그리디)

INPUT :
OUTPUT : 
'''

# 전체 학생 수 n(2~30), 체육복 도난당한 학생들의 번호 배열 lost, 여벌의 체육복 학생 번호 reserve
def solution(n, lost, reserve):
    answer = 0
    
    for i in range(lost):
        if lost[i-1] in reserve or lost[i+1] in reserve:
            
    return answer

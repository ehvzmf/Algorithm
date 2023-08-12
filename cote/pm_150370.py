'''
https://school.programmers.co.kr/learn/courses/30/lessons/150370
프로그래머스 개인정보 수집 유효기간 (문자열)
'''

def time_convert(t) :
    year, month, day = map(int, t.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    term_dict = dict()
    today = time_convert(today)
    answer = []    
    
    for term in terms :
        name, period = term.split()
        term_dict[name] = int(period) * 28
    
    for idx, privacy in enumerate(privacies) :
        start, name = privacy.split()
        end = time_convert(start) + term_dict[name]
        if end <= today :
            answer.append(idx+1)    
    
    return answer

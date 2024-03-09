'''
https://school.programmers.co.kr/learn/courses/30/lessons/42628
프로그래머스 이중우선순위 큐
'''

import heapq

def solution(operations):
    maxh, minh = [], []
    
    for _ in operations:
        op, now = _.split()
        if op == "I":
            heapq.heappush(maxh, -int(now))
            heapq.heappush(minh, int(now))
        elif op == "D":
            if not maxh:
                pass
            elif now == "1":
                minh.remove(-heapq.heappop(maxh))
            elif now == "-1":
                maxh.remove(-heapq.heappop(minh))
    if maxh:
        result = [-heapq.heappop(maxh), heapq.heappop(minh)]
    else:
        result = [0, 0]
    return result

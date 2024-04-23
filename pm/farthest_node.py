'''
https://school.programmers.co.kr/learn/courses/30/lessons/49189
프로그래머스 : 가장 먼 노드 (bfs)
'''

from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    dist = [-1] * (n+1)
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    queue = deque([1]) # 출발 노드 1
    dist[1] = 0
    # max_dist = 0
    
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if dist[i] == -1:
                queue.append(i)
                dist[i] = dist[now] + 1
                # max_dist = max(max_dist, dist[i])
    for d in dist: 
        if d == max(dist):
            answer += 1
    return answer

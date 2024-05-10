'''
https://leetcode.com/problems/path-with-maximum-probability/
4조 스터디 5주차 기초 문제 (다익스트라)
'''

from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        prob = [0.0] * n
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        prob[start_node] = 1.0
        pq = [(-1.0, start_node)]

        while pq:
            cur_prob, cur_v = heappop(pq)

            if cur_v == end_node:
                return -cur_prob
            for next_v, path_prob in graph[cur_v]:
                if -cur_prob * path_prob > prob[next_v]:
                    prob[next_v] = -cur_prob * path_prob
                    heappush(pq, (-prob[next_v], next_v))
        return 0.0

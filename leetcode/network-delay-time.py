'''
https://leetcode.com/problems/network-delay-time/
4조 스터디 5주차 기초 문제 (다익스트라)
'''

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = { i:[] for i in range(1, n+1) }
        for u, v, w in times:
            graph[u].append((v, w))

            dist = {}
            q = [(0, k)] # heapq(w에 따라 정렬) 
            while q:
                wx, x = heappop(q)
                if x not in dist:
                    dist[x] = wx
                    for y, wy in graph[x]:
                        heappush(q, (dist[x] + wy, y))
            if len(dist) == n:
                return max(dist.values())
            return -1

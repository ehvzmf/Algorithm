'''
https://velog.io/@robotroniq/LeetCode-841.-Keys-and-Rooms
4조 스터디 3주차 기초 문제 (그래프)
'''

from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        length = len(rooms)
        visited = [False for _ in range(length)]
        # visited = [False] * length 이렇게 해도 되는데 몰랐던 바보 

        visited[0] = True
        not_visited = length - 1
        q = deque([0])

        while len(q) and not_visited:
            now = q.popleft()
            for key in rooms[now]:
                if not visited[key]:
                    visited[key] = True
                    not_visited -= 1
                    q.append(key)
        
        return False if not_visited else True    

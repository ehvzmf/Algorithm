'''
https://leetcode.com/problems/trapping-rain-water/description/
4조 스터디 2주차 실전 문제 (스택) 

같은 문제: https://www.acmicpc.net/problem/14719
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0

        max_height = max(height)
        for i in range(1, len(height)-1):
            l_max = max(height[:i])
            r_max = max(height[i+1:])

            compare = min(l_max, r_max)

            if height[i] < compare:
                answer += compare - height[i]
        
        return answer

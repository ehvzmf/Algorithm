# https://leetcode.com/problems/count-days-without-meetings/description/
# 2025-03-27
# aystudy

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        flag = [1] * (days + 1)

        for i in range(len(meetings)):
            for j in range(meetings[i][0], meetings[i][1] + 1): 
                flag[j] = 0
        
        answer = sum(flag) - 1
        return answer
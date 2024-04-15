'''
https://leetcode.com/problems/word-search/description/
4조 스터디 1주차 기초 문제 (백트레킹)
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtracking(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'

            found = (backtracking(r+1, c, i+1) or 
                    backtracking(r-1, c, i+1) or
                    backtracking(r, c+1, i+1) or
                    backtracking(r, c-1, i+1))

            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtracking(r, c, 0):
                    return True

        return False 

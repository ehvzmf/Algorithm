'''
https://leetcode.com/problems/n-queens/
4조 스터디 1주차 심화 문제 (백트레킹)
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answers = []
        init = [-1] * n

        def check(board, row, col):
            # 같은 열에 퀸이 있는지 체크
            for i in range(row):
                if board[i] == col or abs(board[i]-col) == row - i:
                    return False
            return True
        
        def n_queens(row, board):
            if row == n: 
                solution = ['.'*col + 'Q' + '.'*(n - col - 1) for col in board]
                answers.append(solution)
                return 
            for col in range(n):
                if check(board, row, col):
                    board[row] = col
                    n_queens(row+1, board)
        
        n_queens(0, init)
        return answers

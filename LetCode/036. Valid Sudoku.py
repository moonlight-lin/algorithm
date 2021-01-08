'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for row in board:
            s = set()
            for n in row:
                if n != '.':
                    if n in s:
                        return False
                    else:
                        s.add(n)
                        
        
        for col in range(9):
            s = set()
            for row in range(9):
                n = board[row][col]
                if n != '.':
                    if n in s:
                        return False
                    else:
                        s.add(n)
                        
        for i in range(0,9,3):
            for j in range(0,9,3):
                s = set()
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        n = board[k][l]
                        if n != '.':
                            if n in s:
                                return False
                            else:
                                s.add(n)
                                
        return True
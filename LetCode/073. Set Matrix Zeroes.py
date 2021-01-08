'''
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        row_size = len(matrix)
        column_size = len(matrix[0])
        
        reset_row = [False] * row_size
        reset_column = [False] * column_size
        
        reset_to_zero = [[False] * column_size for _ in range(row_size)]
        
        for i in range(row_size):
            for j in range(column_size):
                if reset_to_zero[i][j] is True:
                    continue
                    
                if matrix[i][j] == 0:
                    if reset_row[i] is False:
                        reset_row[i] = True
                        for k in range(column_size):
                            if matrix[i][k] != 0:
                                matrix[i][k] = 0
                                reset_to_zero[i][k] = True
                    
                    if reset_column[j] is False:
                        reset_column[j] = True
                        for k in range(row_size):
                            if matrix[k][j] != 0:
                                matrix[k][j] = 0
                                reset_to_zero[k][j] = True
                    
        
        
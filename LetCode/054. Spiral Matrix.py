'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row_size = len(matrix)
        if row_size == 0:
            return []
            
        column_size = len(matrix[0])
        if column_size == 0:
            return []
        
        flag = []
        for _ in range(row_size):
            flag.append([False] * column_size)
            
        RIGHT = 0
        DOWN = 1
        LEFT = 2
        UP = 3
        
        direct = RIGHT
        i = j = 0
        result = []
        for _ in range(row_size * column_size):
            result.append(matrix[i][j])
            flag[i][j] = True
            if direct == RIGHT:
                if j == column_size - 1 or flag[i][j + 1] is True:
                    i += 1
                    direct = DOWN
                else:
                    j += 1
            elif direct == DOWN:
                if i == row_size - 1 or flag[i + 1][j] is True:
                    j -= 1
                    direct = LEFT
                else:
                    i += 1
            elif direct == LEFT:
                if j == 0 or flag[i][j - 1] is True:
                    i -= 1
                    direct = UP
                else:
                    j -= 1
            elif direct == UP:
                if i == 0 or flag[i - 1][j] is True:
                    j += 1
                    direct = RIGHT
                else:
                    i -= 1
                    
        return result
                
                
                
                
                
        
        
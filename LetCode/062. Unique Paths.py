'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        if m == 1 or n == 1:
            return 1
            
        flag = [[1] * n for _ in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                flag[i][j] = flag[i-1][j] + flag[i][j-1]
                
        return flag[-1][-1]
        

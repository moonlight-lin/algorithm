'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Follow up:

Your algorithm should run in O(n) time and uses constant extra space.
'''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        has_one = False
        temp = {}
        for n in nums:
            if n <= 0:
                continue
                
            if n == 1:
                has_one = True
                continue
                
            temp[n] = [False, False]
            if n - 1 in temp:
                temp[n-1][1] = True
                temp[n][0] = True
            if n + 1 in temp:
                temp[n+1][0] = True
                temp[n][1] = True
        
        if has_one is False:
            return 1
        elif 2 not in temp:
            return 2
        else:
            temp[2][0] = True
        
        min = None
        for n in temp.keys():
            if temp[n][0] is False:
                if min is None or min > n - 1:
                    min = n - 1
            elif temp[n][1] is False:
                if min is None or min > n + 1:
                    min = n + 1
                    
        return min
            
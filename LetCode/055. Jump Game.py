'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i][j] <= 10^5
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        '''
        last_pos = len(nums) - 1;
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0
        '''
        
        flag = [True] * len(nums)
        return self.jumpFrom(0, nums, flag)
            
    def jumpFrom(self, position, nums, flag):
        if flag[position] is False:
            return False

        if nums[position] >= len(nums) - position - 1:
            return True
        
        i = nums[position]
        while i > 0:
            if self.jumpFrom(position + i, nums, flag):
                return True
            i -= 1
            
        flag[position] = False
        
        return False
        
        
        
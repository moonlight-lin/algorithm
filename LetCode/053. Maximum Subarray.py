'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_sum = nums[0]
        sum = nums[0] if nums[0] >= 0 else None

        for i in range(1, len(nums)):
            if nums[i] < 0:
                # first non-negative number is not yet found
                if max_sum < 0:
                    # in case all numbers are negative
                    if nums[i] > max_sum:
                        max_sum = nums[i]
                    continue
                   
                # first non-negative number is not yet found after last sequence
                if sum is None:
                    continue
                
                if sum > max_sum:
                    max_sum = sum
            
                sum += nums[i]
                if sum < 0:
                    # set sum as None until next non-negative number is found
                    sum = None
                    continue
            else:
                if sum is None:
                    # this is the first non-negative number
                    sum = nums[i]
                    if max_sum < 0:
                        max_sum = nums[i]
                else:
                    sum += nums[i]
                
                
        if sum is not None and sum > max_sum:
            max_sum = sum
            
        return max_sum
        
        
        
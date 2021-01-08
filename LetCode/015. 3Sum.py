'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        length = len(nums)
        if length < 3:
            return []
            
        nums.sort()
        
        result = []
        
        pre_i = None
    
        for i in range(length):
            if pre_i is None or pre_i != nums[i]:
                pre_i = nums[i]
            else:
                continue

            j = i + 1
            k = length - 1
            
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif sum > 0:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
        return result

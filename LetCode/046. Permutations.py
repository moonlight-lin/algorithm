'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
            
        result_list = []
        for num in nums:
            left_list = nums[:]
            left_list.remove(num)
            left_result_list = self.permute(left_list)
            
            for left_result in left_result_list:
                result = [num]
                result.extend(left_result)
                result_list.append(result)
        return result_list
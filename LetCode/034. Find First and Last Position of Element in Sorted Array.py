'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non decreasing array.
-10^9 <= target <= 10^9
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left = 0
        right = len(nums) - 1
        first = last = -1
        second_round_start = -1
        
        while left <= right:
            mid = (left + right)/2
            if nums[mid] == target:
                first = mid
                right = mid - 1
                
                if second_round_start == -1:
                    second_round_start = mid + 1
                
                if last == -1:
                    last = mid 
            elif nums[left] <= nums[mid]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        if first == -1:
            return [-1, -1]
            
        left = second_round_start
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)/2
            if nums[mid] == target:
                last = mid
                left = mid + 1    
            elif nums[left] <= nums[mid]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return [first, last]
        
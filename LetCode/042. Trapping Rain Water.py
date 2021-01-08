'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        water = 0
        left_bar_map = {}
        
        
        for i in range(len(height)):
            cur_bar = height[i]
            if cur_bar == 0:
                continue
                
            for j in left_bar_map.keys():
                left_bar = left_bar_map[j]
                if left_bar[0] <= cur_bar:
                    water += (left_bar[0] - left_bar[1]) * (i - j - 1)
                    left_bar_map.pop(j)
                elif left_bar[1] < cur_bar:
                    water += (cur_bar - left_bar[1]) * (i - j - 1)
                    left_bar_map[j][1] = cur_bar
                
            left_bar_map[i] = [cur_bar, 0]
        
        return water
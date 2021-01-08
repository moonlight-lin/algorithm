class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        '''
        size = len(height)
        largest_area = 0
        largest_first_index = 0
        largest_second_index = 1
        for first_index in range(0, size - 1):
            for second_index in range(first_index + 1, size):
                area = (second_index - first_index) * min(height[first_index], height[second_index])
                if area > largest_area:
                    largest_area = area
        
        return largest_area
        '''
        
        largest_left_index = 0
        largest_right_index = len(height) - 1
        largest_area = 0
        
        temp_left_index = largest_left_index
        temp_right_index = largest_right_index
        
        while temp_left_index < temp_right_index:
            area = (temp_right_index - temp_left_index) * min(height[temp_left_index], height[temp_right_index])
            if area > largest_area:
                largest_area = area
                largest_left_index = temp_left_index
                largest_right_index = temp_right_index
        
            if height[temp_left_index] <= height[temp_right_index]:
                temp_left_index += 1
            else:
                temp_right_index -= 1
        
        return largest_area
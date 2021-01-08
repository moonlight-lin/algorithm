'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [?231,  231 ? 1]. For the purpose of this problem, assume that your function returns 231 ? 1 when the division result overflows.
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_VALUE = 2147483647
        MIN_VALUE = -2147483648
        
        dividend_is_negative = divisor_is_negative = result_is_negative = False
        
        if dividend < 0:
            dividend = -dividend
            dividend_is_negative = True
        
        if divisor < 0:
            divisor = -divisor
            divisor_is_negative = True
        
        if dividend_is_negative != divisor_is_negative:
            result_is_negative = True
        
        if divisor > dividend:
            return 0
        
        multi_list = []
        multi_result_map = {}
        multi = 1
        multi_result = divisor
        while multi_result <= dividend:
            if result_is_negative is True and -multi <= MIN_VALUE:
                return MIN_VALUE
                
            if result_is_negative is False and multi >= MAX_VALUE:
                return MAX_VALUE
            
            multi_list.append(multi)
            multi_result_map[multi] = multi_result
            multi += multi
            multi_result += multi_result
    
        multi_list_index = len(multi_list) - 1      
        result = 0
        while multi_list_index >= 0:
            multi = multi_list[multi_list_index]
            if multi_result_map[multi] == dividend:
                result += multi
                break
            
            if multi_result_map[multi] < dividend:
                result += multi
                dividend -= multi_result_map[multi]
            
            multi_list_index -= 1
            
        if result_is_negative:
            return -result
        else:
            return result
            
            
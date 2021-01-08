'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [?231,  231 ? 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution(object):
    import math
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        result_str = ""
        
        max_value = math.pow(2,31) - 1
        min_value = -math.pow(2,31)
        
        s = str(x)
        length = len(s)
        if s[0] == "-":
            result_str += "-"
        
        need_to_skip_0 = True       
        i = length - 1
        while i >= 1:
            if need_to_skip_0 and s[i] == "0":
                i -= 1
                continue
            else:
                result_str += s[i]
            need_to_skip_0 = False
            i -= 1
                
        if s[0] != "-":
             result_str += s[0]
             
        result_int = int(result_str)
        if result_int > max_value or result_int < min_value:
             return 0
            
        return result_int

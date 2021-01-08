'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution(object):
    roman_map = {
       "I" : 1,
       "V" : 5,
       "X" : 10,
       "L" : 50,
       "C" : 100,
       "D" : 500,
       "M" : 1000
    }
    
    roman_sub_map = {
        "IV" : 4,
        "IX" : 9,
        "XL" : 40,
        "XC" : 90,
        "CD" : 400,
        "CM" : 900
    }
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s_len = len(s)
        index = 0
        result = 0
        while index < s_len:
            if index < s_len - 1:
                sub = s[index:index+2]
                if sub in self.roman_sub_map:
                    result += self.roman_sub_map[sub]
                    index += 2
                    continue
                    
            result += self.roman_map[s[index]]
            index += 1
            
        return result
        
        
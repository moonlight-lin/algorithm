'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if strs == []:
            return ""

        prefix = ""
        
        string_len = len(strs)
        string_index = 0
        letter_index = 0
        
        while True:
            c = None
            string_index = 0
            while string_index < string_len:
                if letter_index >= len(strs[string_index]):
                    return prefix
                
                if c is None:
                    c = strs[string_index][letter_index]
                elif strs[string_index][letter_index] != c:
                    return prefix
                
                string_index += 1
                
            prefix += c
            letter_index += 1
                
        return prefix
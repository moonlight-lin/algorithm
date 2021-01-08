'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if needle == "":
            return 0
        
        i = j = k = 0
        haystack_len = len(haystack)
        needle_len = len(needle)
        
        for i in range(haystack_len - needle_len + 1):
            for j in range(i, haystack_len):
                if haystack[j] != needle[k]:
                    break
                else:
                    k += 1
                    if k == needle_len:
                        return i
            k = 0
                        
        return -1
            
            
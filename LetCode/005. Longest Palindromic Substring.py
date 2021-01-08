'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        start_index = 0
        end_index = 0
        longest_palindrome_length = 1
        
        length = len(s)
        i = 0
        while i < length - 1:
            left = i - 1
            right = i + 1
            while left >= 0 and right <= length - 1:
                if s[left] == s[right]:
                    left = left - 1
                    right = right + 1
                else:
                    break
                    
            palindrome_length = right - left - 1
            if palindrome_length > longest_palindrome_length:
                longest_palindrome_length = palindrome_length
                start_index = left + 1
                end_index = right - 1
                
            left = i
            right = i + 1
            while left >= 0 and right <= length - 1:
                if s[left] == s[right]:
                    left = left - 1
                    right = right + 1
                else:
                    break
                    
            palindrome_length = right - left - 1
            if palindrome_length > longest_palindrome_length:
                longest_palindrome_length = palindrome_length
                start_index = left + 1
                end_index = right - 1
            
            i += 1
            
        return s[start_index:end_index+1]
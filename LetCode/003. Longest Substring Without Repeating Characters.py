'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        start_index = 0
        longest = 0
        letter_dict = {}
        for cur_index, c in enumerate(s):
            if c in letter_dict:
                if letter_dict[c] >= start_index:
                    start_index = letter_dict[c] + 1
                    if length > longest:
                        longest = length

                    length = cur_index - start_index + 1
                else:
                    length += 1
            else:
                length += 1
            
            letter_dict[c] = cur_index
        
        if length > longest:
            return length
        else:
            return longest

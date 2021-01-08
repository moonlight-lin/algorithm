'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = [[strs[0]]]
        sorted_result = [sorted(strs[0])]
        
        for i in range(1, len(strs)):
            match_any = False
            sorted_word_to_cmp = sorted(strs[i])
            
            for j in range(0, len(sorted_result)):
                if sorted_word_to_cmp == sorted_result[j]:
                    result[j].append(strs[i])
                    match_any = True
                    break
                    
            if not match_any:
                result.append([strs[i]])
                sorted_result.append(sorted_word_to_cmp)
        
        return result
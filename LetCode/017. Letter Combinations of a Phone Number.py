'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''
class Solution(object):
    digit_map = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
    }
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        result = []
        
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            for letter in self.digit_map[digits[0]]:
                result.append(letter)
            return result
        else:
            result_tmp = self.letterCombinations(digits[1:])
            for letter in self.digit_map[digits[0]]:
                i = 0
                while i < len(result_tmp):
                    result.append(letter + result_tmp[i])
                    i += 1
            return result
                
                
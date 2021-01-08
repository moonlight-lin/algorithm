'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution(object):
    def generateParenthesis(self, n, prefix = "", not_matched_in_prefix = 0):
        """
        :type n: int
        :rtype: List[str]
        """
        
        if n == 0:
            return [prefix + ")" * not_matched_in_prefix]
        
        if not_matched_in_prefix == 0:
            result = self.generateParenthesis(n - 1, prefix + "(", 1)
        else:
            result = self.generateParenthesis(n - 1, prefix + "(", not_matched_in_prefix + 1)
            result.extend(self.generateParenthesis(n, prefix + ")", not_matched_in_prefix - 1))
        
        return result



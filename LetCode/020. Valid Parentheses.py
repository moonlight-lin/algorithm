'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''

class Solution(object):
    bracket_map = {
        "}": "{",
        ")": "(",
        "]": "["
    }
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s == "":
            return True
            
        stack = []
        for c in s:
            if c in self.bracket_map:
                if not stack or stack.pop() != self.bracket_map[c]:
                    return False
            else:
                stack.append(c)
                
        return not stack
        
        
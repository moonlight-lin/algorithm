'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        ''' Long Time Exceed
        if not p:
            return not s

        new_p = ""
        pre_c = None
        for c in p:
            if c != "*":
                new_p += c
                pre_c = c
            else:
                if pre_c != "*":
                    new_p += c
                    pre_c = "*"
        p = new_p

        if not s:
            return p == "*"

        if p[0] == "*":
            return (self.isMatch(s[1:], p[0:])) or (self.isMatch(s, p[1:]))

        first_match = bool(s) and p[0] in {s[0], '?'}

        return first_match and self.isMatch(s[1:], p[1:])
        '''

        if p is not None:
            new_p = ""
            pre_c = None
            for c in p:
                if c != "*" or pre_c != "*":
                    new_p += c
                    pre_c = c
            p = new_p

        if not p:
            return not s

        if not s:
            return p == "*"

        p_len = len(p)
        s_len = len(s)

        index = 0
        while True:
            if p[index] == '*':
                if index == p_len - 1:
                    return True
                break
            elif p[index] != s[index] and p[index] != '?':
                return False
            index += 1
            if index == p_len and index == s_len:
                return True
            elif index == p_len:
                return False
            elif index == s_len:
                return p[index:] == "*"
        first_star = first_c = index

        p_index = p_len - 1
        s_index = s_len - 1
        while True:
            if p[p_index] == '*':
                break
            elif p[p_index] != s[s_index] and p[p_index] != '?':
                return False
            p_index -= 1
            s_index -= 1
            if p_index == first_star:
                return True
            elif s_index < first_star:
                return False
        last_star = p_index
        last_c = s_index

        p_list = p[first_star+1:last_star].split("*")
        index = first_c
        for sub_p in p_list:
            sub_p_len = len(sub_p)
            while True:
                sub_p_index = 0
                sub_c_index = index
                while sub_c_index <= last_c and sub_p_index < sub_p_len:
                    if sub_p[sub_p_index] != s[sub_c_index] and sub_p[sub_p_index] != '?':
                        break
                    sub_c_index += 1
                    sub_p_index += 1
                if sub_p_index == sub_p_len:
                    index = sub_c_index
                    break
                elif index > last_c:
                    return False
                else:
                    index += 1

        return True



class Solution:
    def isValid(self, s: str) -> bool:
        self.s = s
        
        s_copy = []
        openings = ["(",  "{", "["]
        closings = [')', '}', ']']
        valid_pairs = ['()', '{}', '[]']

        for i in self.s:
            if i in openings:
                s_copy.append(i)
            if i in closings:
                if not s_copy:
                    return False
                elif s_copy.pop() + i not in valid_pairs:
                    return False
        if len(s_copy):
            return False
        return True

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
"""
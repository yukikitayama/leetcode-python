"""
- Failed
"""


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_open = 0
        curly_bracket_open = 0
        square_bracket_open = 0

        for char in s:
            if char == '(':
                bracket_open += 1
            elif char == ')':
                bracket_open -= 1
                if bracket_open < 0:
                    return False
            elif char == '{':
                curly_bracket_open += 1
            elif char == '}':
                curly_bracket_open -= 1
                if curly_bracket_open < 0:
                    return False
            elif char == '[':
                square_bracket_open += 1
            elif char == ']':
                square_bracket_open -= 1
                if square_bracket_open < 0:
                    return False

        if bracket_open == 0 and curly_bracket_open == 0 and square_bracket_open == 0:
            return True
        else:
            return False


s = "()"
s = "()[]{}"
s = "(]"
s = "([)]"
print(Solution().isValid(s))


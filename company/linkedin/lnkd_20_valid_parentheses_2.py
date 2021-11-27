"""
- Use stack
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_to_open = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif char in [')', '}', ']']:
                if stack and close_to_open[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


s = "()"
s = "()[]{}"
# s = "(]"
# s = "([)]"
# s = '['
print(Solution().isValid(s))


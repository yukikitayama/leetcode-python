"""
Stack
"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []

        for ch in s:

            if len(stack) >= 2 and ch == stack[-1] and ch == stack[-2]:
                continue

            stack.append(ch)

        return "".join(stack)

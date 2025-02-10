"""
stack collects non-digit
pop if current character is digit
"""


class Solution:
    def clearDigits(self, s: str) -> str:

        stack = []

        for ch in s:

            if ch.isalpha():

                stack.append(ch)

            else:
                stack.pop()

        return "".join(stack)

"""
Stack
  append current character
  if stack top character is same as the current character
    pop stack top
    this current character don't append to stack
  otherwise append to stack
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []

        for i in range(len(s)):

            ch = s[i]

            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)

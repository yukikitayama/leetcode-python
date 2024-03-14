"""
Stack contains number and character together
pop when ]
  pop until number
"""


class Solution:
    def decodeString(self, s: str) -> str:
        ans = []
        stack = []
        i = 0

        while i < len(s):

            if s[i].isdigit():

                curr = 0
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1
                stack.append(curr)

            elif s[i].isalpha():

                curr = []
                while i < len(s) and s[i].isalpha():
                    curr.append(s[i])
                    i += 1
                stack.append("".join(curr))

            elif s[i] == "]":
                curr = []

                while not isinstance(stack[-1], int):
                    curr.append(stack.pop())
                curr.reverse()
                chars = "".join(curr)
                num = stack.pop()
                stack.append(num * chars)

                i += 1

            else:
                i += 1

            # print(stack)

        return "".join(stack)
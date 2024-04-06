"""
Stack to save processed string
iterate from left to right
  if balance is negative with ")",
    don't push to stack
iterate from right to left
  if balance is negative with "(",
    don't push to stack

"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        balance = 0
        for i in range(len(s)):

            if s[i] == "(":
                balance += 1
            elif s[i] == ")":
                balance -= 1

            if balance >= 0:
                stack.append(s[i])
            else:
                balance = 0
                continue

        # print(stack)

        s = "".join(stack)
        stack = []
        balance = 0
        for i in range(len(s) - 1, -1, -1):

            if s[i] == ")":
                balance += 1
            elif s[i] == "(":
                balance -= 1

            if balance >= 0:
                stack.append(s[i])
            else:
                balance = 0
                continue

        stack.reverse()
        # print(stack)

        return "".join(stack)

"""
iterate from left to right
  collect to buffer
balance
  increment with (
  decrement with )
when balance is negative, remove )
  reset the balance to 0
after iteration
  when balance is 0,
    good, return collected string and ()
  if balance is positive
    there are remaining (
    e.g., "abc((", balance: 2
    scan from right to left
      buffer [c, b, a]
    reverse buffer to return

s = "lee(t(c)o)de)"
s = "a)b(c)d",
s = "))(("
s = "))(()"
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        balance = 0
        buffer = []

        # Left to right
        for i in range(len(s)):
            if s[i] == "(":
                balance += 1
            elif s[i] == ")":
                balance -= 1

            if balance < 0:
                balance = 0
            else:
                buffer.append(s[i])

        if balance == 0:
            return "".join(buffer)

        # Positive balance
        # Right to left
        s = "".join(buffer)
        balance = 0
        buffer = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ")":
                balance += 1
            elif s[i] == "(":
                balance -= 1

            if balance < 0:
                balance = 0
            else:
                buffer.append(s[i])

        buffer.reverse()
        return "".join(buffer)


"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()
        s = list(s)

        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            elif char == ")":
                if stack:
                    stack.pop()
                else: 
                    s[index] = ""

        while stack:
            s[stack.pop()] = ""
        return ''.join(s)
"""


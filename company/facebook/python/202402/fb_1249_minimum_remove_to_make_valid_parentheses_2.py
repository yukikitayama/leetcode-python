"""
balance
iteration
  collectio valid character to stack
  if balance is negative
    current close won't be appended to collection

after iteration
  if balance is positive
  pop from the stack
    save to another stack
    if current is open
      don't save to another stack

join the second stack, by popping from the top as answer

eg,
  "a)b(c)(d"
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        def delete_invalid(s, open_, close):
            balance = 0
            stack = []

            for i in range(len(s)):

                curr = s[i]

                if curr == open_:
                    balance += 1
                elif curr == close:
                    balance -= 1

                if balance < 0:
                    balance = 0
                    continue
                else:
                    stack.append(curr)

            return "".join(stack)

        ans = delete_invalid(s, "(", ")")
        ans = delete_invalid(ans[::-1], ")", "(")
        return ans[::-1]

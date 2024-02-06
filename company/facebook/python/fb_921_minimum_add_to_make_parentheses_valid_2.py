"""
only insert, not remove

balance
  +1 if (
  -1 if )

if close appears earlier than close, trouble

ans = 0

iterate s
  update balance
  when balance is negative
    increment ans and reset balance

and remaining balance to ans

"()))(("
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        ans = 0

        balance = 0

        for i in range(len(s)):
            if s[i] == "(":
                balance += 1
            elif s[i] == ")":
                balance -= 1

            if balance < 0:
                ans += 1
                balance = 0

        return ans + balance
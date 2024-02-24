"""
())()
  balance negative in middle
    add open
)()
  same
()(
  balance positive end
    add close
()(()
  open in middle but same as positive end
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        ans = 0
        balance = 0

        for i in range(len(s)):
            curr = s[i]

            if curr == "(":
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                ans += 1
                balance = 0

        if balance > 0:
            ans += balance
        # There is no ending with negative balance

        return ans

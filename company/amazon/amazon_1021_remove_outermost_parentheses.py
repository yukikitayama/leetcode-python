"""
primitive happens when balance is 0
two pointers
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []

        balance = 0
        left = 0

        for right in range(len(s)):

            if s[right] == "(":
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                ans.append(s[left + 1:right])
                left = right + 1

        return "".join(ans)

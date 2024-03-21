"""
two passes
  left to right
  remove ) when balance is -1
  right to left
  remove ( when balance is -1
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        balance = 0
        ans = []

        # From left to right
        for i in range(len(s)):

            if s[i] == "(":
                balance += 1
            elif s[i] == ")":
                balance -= 1

            if balance < 0:
                balance = 0
            else:
                ans.append(s[i])

        # print("ans", ans)

        # From right to left
        ans2 = []
        balance = 0
        for i in range(len(ans) - 1, -1, -1):

            # "()("
            if ans[i] == "(":
                balance -= 1
            elif ans[i] == ")":
                balance += 1

            if balance < 0:
                balance = 0
            else:
                ans2.append(ans[i])

        ans2.reverse()

        # print("ans2", ans2)

        return "".join(ans2)

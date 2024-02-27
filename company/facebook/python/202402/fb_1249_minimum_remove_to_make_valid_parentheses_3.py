"""
)()
())
balance negative
  once negative remove
(()
()(
after iteration, remaining positive balance, need to remove
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        balance = 0
        opens = 0

        first_pass = []

        for i in range(len(s)):

            if s[i] == "(":
                balance += 1
                opens += 1
            elif s[i] == ")":
                balance -= 1

            if balance < 0:
                balance = 0
                continue

            first_pass.append(s[i])

        ans = []
        num_open_include = opens - balance

        for i in range(len(first_pass)):

            if first_pass[i] == "(":
                if num_open_include > 0:
                    ans.append(first_pass[i])
                num_open_include -= 1

            else:
                ans.append(first_pass[i])

        return "".join(ans)

    def minRemoveToMakeValid1(self, s: str) -> str:

        balance = 0

        chars = [ch for ch in s]
        ans = []

        for i in range(len(chars)):

            if chars[i] == ")":
                balance -= 1
            elif chars[i] == "(":
                balance += 1

            if balance < 0:
                balance = 0
                continue
            else:
                ans.append(chars[i])

        # Pop open from right by remaining balance times
        tmp = []
        while balance:
            top = ans.pop()
            if top == "(":
                balance -= 1
            else:
                tmp.append(top)
        while tmp:
            ans.append(tmp.pop())

        return "".join(ans)
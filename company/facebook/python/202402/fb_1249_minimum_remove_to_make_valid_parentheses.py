"""
iterate from left to right
  count '(' and ')'
  remove ')' if '(' has not been seen
  remove ')' if the number of ')' exceeds the number of '(' which has been seen so far

at the end, if ( num > ) num, remove (
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        count_open = 0
        count_close = 0

        ans = []

        for i in range(len(s)):

            if s[i] not in ["(", ")"]:
                ans.append(s[i])

            elif s[i] == ")" and count_open == 0:
                continue

            elif s[i] == "(":
                ans.append(s[i])
                count_open += 1

            elif s[i] == ")" and count_close < count_open:
                ans.append(s[i])
                count_close += 1

            elif s[i] == ")" and count_close == count_open:
                continue

        return "".join(ans)



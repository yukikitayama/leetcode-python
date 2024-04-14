"""
Input: s = "1?:?4"
Output: "11:54"

Input: s = "0?:5?"
Output: "09:59"

1st digit
  0
    2nd digit 0-9
    00, 01, 02, ... 09
  1
    2nd digit 0-1
    10, 11
3rd digit
  0-5
4th digit
  0-9
"""


class Solution:
    def findLatestTime(self, s: str) -> str:
        ans = list(s)

        if s[0] == "?" and s[1] == "?":
            ans[0] = "1"
            ans[1] = "1"
        elif s[0] == "?" and s[1] != "?":
            if s[1] in ["0", "1"]:
                ans[0] = "1"
            else:
                ans[0] = "0"
        elif s[0] != "?" and s[1] == "?":
            if s[0] == "0":
                ans[1] = "9"
            elif s[0] == "1":
                ans[1] = "1"

        if s[3] == "?":
            ans[3] = "5"

        if s[4] == "?":
            ans[4] = "9"

        return "".join(ans)


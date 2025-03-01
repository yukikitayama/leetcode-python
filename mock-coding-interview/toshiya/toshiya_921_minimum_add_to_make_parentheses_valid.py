"""
s = "())"
"": valid
"(": not valid
"()": valid where A = ""
B: "()"
s = "B)"
create "(B)" = "(())"

")("
"()("
"()()"
count number of open and close from left to right
  when open
    +1
  when close
    -1
  if we get negative
    we need one opening
    reset to 0
      ")", "()",
After iterating
  if positive
    need number of inserts by the positive amount
s = "())"
"())"
  "(())"
  "()()"

")))((", 3 for inserting openings + 2 for inserting closing
"()()()()", 0
"((()(", 3, "()()()()"
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        ans = 0

        for ch in s:

            if ch == "(":
                balance += 1

            elif ch == ")":
                balance -= 1

            if balance < 0:
                ans += 1
                balance = 0

        return ans + balance if balance > 0 else ans
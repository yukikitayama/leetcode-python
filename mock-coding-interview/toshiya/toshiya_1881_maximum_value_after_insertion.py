"""
n: 73
  len: 2
  number of patterns: 3 (673, 763, 736)
x: 6

n: 77
x: 6
  (677, 767, 776)

n: 6543321
x: 3

n: -654321
x: 3
  -6543321
  -3654321

positive case > 0
  no "-" at the leftmost of n
  iterate digit in n from left to right
    when x is bigger than the current difit, insert

negative case < 0
  "-" at the leftmost
  iterate difit in n from left to right
    if x is smaller than the current digit, insert

0 case

Simulation

N is length of n
T: O(N)
S: O(N)
"""


class Solution:
    def maxValue(self, n: str, x: int) -> str:
        ans = []
        is_positive = n[0] != "-"
        used_x = False

        for ch in n:

            if is_positive:
                if x > int(ch) and not used_x:
                    ans.append(str(x))
                    used_x = True
                ans.append(ch)

            else:
                if ch == "-":
                    ans.append(ch)
                else:
                    if x < int(ch) and not used_x:
                        ans.append(str(x))
                        used_x = True
                    ans.append(ch)

        if not used_x:
            ans.append(str(x))

        return "".join(ans)

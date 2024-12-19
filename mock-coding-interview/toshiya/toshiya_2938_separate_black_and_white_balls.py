"""
Simulate
  s: 11111101, 11111011
Don't simulate
  for each 0's index, index is just distance

  s: 11110101
  s: 01111101
  s: 00111111
    1st 0: 4
    2nd 0: 6 - 1 = 5

ans = 0
num_zero
Iterate from left
  if I see 0,
    increment ans by index of 0
    and decrement by the number of 0 you saw so far
"""

class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        num_zeros = 0

        for i in range(len(s)):

            if s[i] == "0":
                ans += i
                ans -= num_zeros
                num_zeros += 1

        return ans
"""
"11106"
  1, 1, 1, 0 (invalid)
  1, 1, 10, 6
  1, 11, 0 (invalid)
  11, 1, 0,
  11, 10, 6
1. finish current digit, and start a new digit
  1, [1], 1,
2. continue current digit
  1, [11] -> next

1. 1 digit
  current digit 1 to 9
  next i+1
2. 2 digits
  if current digit is 1 or 2,
    if 1, then next digit is 0 to 9
    if 2, then next digit is 0 to 6
  next i+2
if current digit is 0, invalid

DFS, backtracking

T: O(2 ** 100) = huge

if backtracking doesn't work
  dynamic programming
"""

import functools


class Solution:
    def numDecodings(self, s: str) -> int:

        @functools.lru_cache(maxsize=None)
        def backtracking(index):

            # Termination
            if index == len(s):
                return 1

            if s[index] == "0":
                return 0

            res = 0

            # 1 digit
            res += backtracking(index + 1)

            # 2 digits
            if s[index] == "1":

                if index < len(s) - 1:
                    res += backtracking(index + 2)

            if s[index] == "2":

                if index < len(s) - 1 and s[index + 1] in "0123456":
                    res += backtracking(index + 2)

            return res

        return backtracking(0)

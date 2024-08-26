"""
n: 1
  already one A
  0
n: 2
  copy one A
  paste one A, have AA
  2
n: 3
  copy one A
  paste one A,
  paste one A, have AAA
  3
n: 4
  copy one A
  paste one A, have AA
  copy two A2
  paste two As, have AAAA
  4
n: 5
  copy one A
  paste one A, have AA
  paste one A
  paste one A
  paste one A, have AAAAA
  5
n: 6
  copy one A
  paste one A, have AA
  copy two A2,
  paste two As, have AAAA
  paste two As, have AAAAAA
  5
"""

import functools


class Solution:
    def minSteps(self, n: int) -> int:

        @functools.cache
        def recursion(curr_len, prev_len):

            if curr_len == n:
                return 0

            elif curr_len > n:
                return float("inf")

            res = float("inf")

            # Copy and paste
            res = min(
                res,
                2 + recursion(curr_len * 2, curr_len)
            )

            # Paste
            res = min(
                res,
                1 + recursion(curr_len + prev_len, prev_len)
            )

            return res

        # Edge case: no prev paste doesn't exist
        if n == 1:
            return 0

        else:
            # 1 by assuming previous copy happened
            return 1 + recursion(1, 1)

"""
eg1
  sum: 24
  rolls sum: 12
  total sum - rolls sum = 24 - 12 = 12
  12 / n = 12 / 2 = 6
eg2
  sum: 21
  rolls sum: 12
  total sum - rolls sum = 21 - 12 = 9 (remaining) 3
eg3
  sum: 6 * (4 + 4) = 48
  rolls sum: 10
  n array sum: 48 - 10 = 38
    38 / n = 38 / 4 = 9._
rule
  if remaining >= n and remaining <= n * 6
    then distributable
"""

from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = mean * (m + n)
        remaining = total_sum - sum(rolls)

        # Edge case
        if remaining / n > 6:
            return []

        def create_array(remain):
            res = [0] * n
            i = 0
            # re
            while remain > 0:
                res[i] += 1
                i += 1
                i %= n
                remain -= 1
            return res

        if n <= remaining <= n * 6:
            return create_array(remaining)
        else:
            return []
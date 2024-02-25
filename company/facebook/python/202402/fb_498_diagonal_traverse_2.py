"""
[(0, 0)]
[(1, 0), (0, 1)]
[(2, 0), (1, 1), (2, 0)]

Sum of row and col are identical
If sum is odd, reverse
Collect bottom right to top left
Hashmap
  k: sum
  v: list of vals
"""

from typing import List
import collections


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        sum_to_vals = collections.defaultdict(list)
        for r in range(len(mat) - 1, -1, -1):
            for c in range(len(mat[0]) - 1, -1, -1):
                sum_ = r + c
                sum_to_vals[sum_].append(mat[r][c])

        ans = []
        max_sum = max(sum_to_vals.keys())
        for i in range(max_sum + 1):
            if i % 2 == 0:
                ans.extend(sum_to_vals[i])
            elif i % 2 != 0:
                vals = sum_to_vals[i]
                vals.reverse()
                ans.extend(vals)
        return ans

"""
eg1
  minimum length of ribbons
eg2
  more k than the number of ribbons
    we need to cut a ribbon to have more number of ribbons
    cut from the longest ribbon
      try to get the minimu length and see if we can get twice min length
        if not decrement length by 1
        9 -> 5 and 4
        9 -> 4 and 4 and 1
eg3
  sum of lengths: 21 < k, so impossible

Observations
  sum of ribbons <= k to make max possible positive integer > 0
  when num ribbons is equal to k, min ribbon is the answer
"""

from typing import List


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:

        if sum(ribbons) < k:
            return 0

        def compute_num_ribbons_by_cutting(length):
            ans = 0

            for ribbon in ribbons:
                num_ribbon = ribbon // length
                ans += num_ribbon

            return ans

        # Binary search the largest length of ribbon
        left = 0
        right = max(ribbons)

        while left < right:

            # When elements are even
            # l + (r - l) // 2 gives former, avoid l = mid, because in [0, 1], l: 0, r: 1, mid: 0, doesn't shrink
            # l + (r - l + 1) // 2 gives latter, avoid r = mid, because in [0, 1], l: 0, r: 1, mid: 1, doesn't shrink
            # +1 because in [0, 1], we wanna have 1, otherwise zero devision cause error
            mid = left + (right - left + 1) // 2

            if compute_num_ribbons_by_cutting(mid) >= k:
                # Try longer ribbon
                left = mid

            # Try shorter ribbon
            else:
                right = mid - 1

        return left



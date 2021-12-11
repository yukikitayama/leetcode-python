"""
Idea
- 3 states
  - i for index at multipliers
  - left for left index in nums
  - right for right index in nums
    - n: nums length, right = n - 1 (i - left)
      because i is the total elements we have picked,
      i - left is the number of elements picked from right.
- dp(i, left) represents the maximum possible score if we have done i operations
  and used left elements from the left side.
"""


from typing import List
import functools


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        @functools.lru_cache(maxsize=2000)
        def dp(i, left):
            if i == m:
                return 0

            mult = multipliers[i]
            right = n - 1 - (i - left)

            return max(
                mult * nums[left] + dp(i + 1, left + 1),
                mult * nums[right] + dp(i + 1, left)
            )

        n = len(nums)
        m = len(multipliers)
        return dp(0, 0)





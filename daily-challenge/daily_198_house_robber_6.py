"""
dp(i)
  base case
    i < 0, return 0
    rob current and rob i - 2
    no rob current and rob i - 1
  argument
    index to nums
  return
    max money to rob up to nums[i]
"""

from typing import List
import functools


class Solution:
    def rob(self, nums: List[int]) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(i):

            # Base case
            if i < 0:
                return 0

            return max(
                # Rob curr house and skip next
                nums[i] + dp(i - 2),
                # Skip curr house and go to next
                dp(i - 1)
            )

        return dp(len(nums) - 1)


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    nums = [2, 7, 9, 3, 1]
    print(Solution().rob(nums))

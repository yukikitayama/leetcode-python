"""
dp(i)
  function
    checks whether a valid partition exist for the prefix subarray nums[0 to i]
    base case
      if i < 0, return T
  argument
    index to nums
  return
    boolean
      T if nums[i] == nums[i - 1] and dp(i - 2) is T
      T if nums[i] == nums[i - 1] == nums[i - 2] and dp(i - 3) is T
      T if nums[1] == nums[i - 1] + 1 == nums[i - 2] + 2 and dp(i - 3) is T

1, 2, 3, 4
  1 | 2, 3, 4
    1 | 2 | 3, 4
    1 | 2, 3 | 4
  1, 2 | 3, 4
    1 | 2 | 3, 4
    1, 2 | 3 | 4
  1, 2, 3 | 4
"""

from typing import List
import functools


class Solution:
    def validPartition(self, nums: List[int]) -> bool:

        @functools.lru_cache(maxsize=None)
        def dp(i):

            if i < 0:
                return True

            ans = False

            if i > 0 and nums[i] == nums[i - 1]:
                ans |= dp(i - 2)
            if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:
                ans |= dp(i - 3)
            if i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:
                ans |= dp(i - 3)

            return ans

        return dp(len(nums) - 1)


if __name__ == "__main__":
    pass

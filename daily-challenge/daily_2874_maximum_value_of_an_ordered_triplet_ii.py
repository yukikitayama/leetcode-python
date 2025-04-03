"""
if j is fixed,
  get max i from left
  get max k from right

if k is fixed
"""

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        max_diff = 0
        max_i = 0

        for k in range(len(nums)):
            ans = max(
                ans,
                max_diff * nums[k]
            )

            # Here nums[k] is j
            max_diff = max(
                max_diff,
                max_i - nums[k]
            )

            # Here nums[k] is i
            max_i = max(
                max_i,
                nums[k]
            )

        return ans

    def maximumTripletValue1(self, nums: List[int]) -> int:
        max_is = [0] * len(nums)
        max_ks = [0] * len(nums)
        for j in range(1, len(nums)):
            # [1, 2, 3], [0, 1, 2]
            max_is[j] = max(max_is[j - 1], nums[j - 1])
            # n: 4, j: 1, index: 4 - 1 - 1
            max_ks[len(nums) - j - 1] = max(max_ks[len(nums) - j], nums[len(nums) - j])

        ans = 0
        for j in range(1, len(nums) - 1):
            ans = max(
                ans,
                (max_is[j] - nums[j]) * max_ks[j]
            )

        return ans

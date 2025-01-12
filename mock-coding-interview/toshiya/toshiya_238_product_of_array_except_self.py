"""
Preprocess
prefix product
  [1, 2, 6, 24]
suffix product
  [24, 24, 12, 4]
ans
  [24, 12, 8, _]
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Prefix
        prefixs = [None] * len(nums)
        prefixs[0] = nums[0]
        for i in range(1, len(nums)):
            prefixs[i] = prefixs[i - 1] * nums[i]

        # Suffix
        suffixs = [None] * len(nums)
        suffixs[-1] = nums[-1]
        for i in range(len(nums) - 1 - 1, -1, -1):
            suffixs[i] = suffixs[i + 1] * nums[i]

        # print(prefixs)
        # print(suffixs)

        # Populate answer
        ans = [None] * len(nums)
        for i in range(len(nums)):

            if i == 0:
                ans[i] = suffixs[i + 1]

            elif i == len(nums) - 1:
                ans[i] = prefixs[i - 1]

            else:
                ans[i] = prefixs[i - 1] * suffixs[i + 1]

        return ans

"""
n: 4
i: 0
i + 1: 1
n - i - 1: 2

n: 4
i: 1
i + 1: 2
n - i - 1: 2

total sum
current sum
"""

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        total = sum(nums)
        prefix = 0
        ans = 0

        for i in range(len(nums) - 1):

            prefix += nums[i]
            right = total - prefix
            if prefix >= right:
                ans += 1

        return ans

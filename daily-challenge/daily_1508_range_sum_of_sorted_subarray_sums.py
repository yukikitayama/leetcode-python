"""
n * (n + 1) / 2 is
"""

from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray_sums = []
        for l in range(len(nums)):
            sum_ = 0
            for r in range(l, len(nums)):
                sum_ += nums[r]
                subarray_sums.append(sum_)
        subarray_sums.sort()

        # print(subarray_sums)

        return sum(subarray_sums[left - 1:right]) % (10 ** 9 + 7)
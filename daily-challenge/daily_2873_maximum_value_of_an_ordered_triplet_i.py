"""
when j and k are fixed, get max nums[i] to maximize (nums[i] - nums[j]) * nums[k]

when j is fixed,
  get max nums[i] from [0, j)
  get max nums[k] from [j + 1, n)

when k is fixed
  triplet is maximized when difference of i and j is max
  keep max_i and max_diff
"""

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        max_diff = 0
        max_nums_i = 0
        for k in range(len(nums)):
            res = max(
                res,
                max_diff * nums[k]
            )

            # nums[k] acts as nums[j]
            max_diff = max(
                max_diff,
                max_nums_i - nums[k]
            )

            # nums[k] act as nums[i]
            max_nums_i = max(
                max_nums_i,
                nums[k]
            )

        return res

    def maximumTripletValue3(self, nums: List[int]) -> int:
        left_max = [0] * len(nums)
        right_max = [0] * len(nums)
        for i in range(1, len(nums)):
            left_max[i] = max(
                left_max[i - 1],
                nums[i - 1]
            )
            right_max[len(nums) - 1 - i] = max(
                right_max[len(nums) - i],
                nums[len(nums) - i]
            )

        res = 0
        for j in range(1, len(nums) - 1):
            res = max(
                res,
                (left_max[j] - nums[j]) * right_max[j]
            )

        return res

    def maximumTripletValue2(self, nums: List[int]) -> int:
        res = 0

        for k in range(2, len(nums)):
            max_nums_i = nums[0]
            for j in range(1, k):
                res = max(
                    res,
                    (max_nums_i - nums[j]) * nums[k]
                )
                max_nums_i = max(
                    max_nums_i,
                    nums[j]
                )

        return res

    def maximumTripletValue1(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    ans = max(
                        ans,
                        (nums[i] - nums[j]) * nums[k]
                    )

        return ans
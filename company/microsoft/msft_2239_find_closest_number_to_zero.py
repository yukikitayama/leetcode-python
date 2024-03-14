from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_diff_so_far = float("inf")
        ans = float("-inf")

        for i in range(len(nums)):

            abs_diff = abs(nums[i] - 0)

            if abs_diff < min_diff_so_far:

                ans = nums[i]
                min_diff_so_far = abs_diff

            elif abs_diff == min_diff_so_far:
                ans = max(ans, nums[i])

        return ans

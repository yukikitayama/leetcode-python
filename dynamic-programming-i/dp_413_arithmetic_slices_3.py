from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = 0
        sum = 0

        for i in range(2, len(nums)):

            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp = dp + 1
                sum += dp
            # Reset dp
            else:
                dp = 0

        return sum


"""
Bottom up dynamic programming with a constant space
"""


nums = [1,2,3,4]

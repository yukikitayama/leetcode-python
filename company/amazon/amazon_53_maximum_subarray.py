"""
Expand as long as positive
Shrink if negative
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        curr_sum = 0

        for num in nums:
            curr_sum = max(0, curr_sum) + num
            ans = max(ans, curr_sum)

        return ans

    def maxSubArray1(self, nums: List[int]) -> int:
        ans = nums[0]
        for left in range(len(nums)):
            curr_sum = 0
            for right in range(left, len(nums)):
                curr_sum += nums[right]
                ans = max(ans, curr_sum)

        return ans

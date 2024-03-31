"""
Sliding window
Increment ans by right - left + 1 in each iteration
Contract while right is same as right's previous
"""

from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        for right in range(len(nums)):

            while right > 0 and left < right and nums[right] == nums[right - 1]:
                left += 1

            ans += right - left + 1

        return ans

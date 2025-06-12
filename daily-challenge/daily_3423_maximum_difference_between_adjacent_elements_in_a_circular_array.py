from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):

            ans = max(
                ans,
                abs(nums[i] - nums[(i + 1) % len(nums)])
            )

        return ans
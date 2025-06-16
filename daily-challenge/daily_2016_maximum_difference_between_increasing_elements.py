from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        min_ = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > min_:
                ans = max(
                    ans,
                    nums[i] - min_
                )
            # If current num is equal to previous min or smaller than current min, update min to get the minimum so far.
            else:
                min_ = nums[i]
        return ans

    def maximumDifference1(self, nums: List[int]) -> int:
        ans = -1
        left = 0
        right = len(nums) - 1
        min_ = float("inf")
        max_ = float("-inf")
        while left < right:
            min_ = min(min_, nums[left])
            max_ = max(max_, nums[right])
            ans = max(ans, max_ - min_)

            left += 1
            right -= 1

        return ans
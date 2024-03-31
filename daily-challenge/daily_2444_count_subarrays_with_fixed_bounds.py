from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        recent_min_idx = recent_max_idx = recent_invalid_idx = -1
        ans = 0

        for right in range(len(nums)):

            if nums[right] < minK or maxK < nums[right]:
                recent_invalid_idx = right

            if nums[right] == minK:
                recent_min_idx = right

            if nums[right] == maxK:
                recent_max_idx = right

            left_valid_rightmost = min(recent_min_idx, recent_max_idx)
            if left_valid_rightmost - recent_invalid_idx < 0:
                continue
            else:
                ans += left_valid_rightmost - recent_invalid_idx

        return ans
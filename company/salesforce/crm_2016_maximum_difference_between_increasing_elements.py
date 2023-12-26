from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1

        min_so_far = nums[0]

        for i in range(1, len(nums)):

            if min_so_far < nums[i]:
                ans = max(ans, nums[i] - min_so_far)

            if nums[i] < min_so_far:
                min_so_far = nums[i]

        return ans
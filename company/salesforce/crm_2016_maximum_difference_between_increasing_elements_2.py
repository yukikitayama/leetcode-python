from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        min_so_far = nums[0]
        ans = -1

        for i in range(1, len(nums)):

            if nums[i] > min_so_far:
                ans = max(ans, nums[i] - min_so_far)

            else:
                min_so_far = nums[i]

        return ans

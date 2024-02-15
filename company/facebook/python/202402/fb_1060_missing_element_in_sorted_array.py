from typing import List


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):

            missing = nums[i] - nums[i - 1] - 1

            if missing >= k:
                return nums[i - 1] + k

            else:
                k -= missing

        if k > 0:
            return nums[-1] + k
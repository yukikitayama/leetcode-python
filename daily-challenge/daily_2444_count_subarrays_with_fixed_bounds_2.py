from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0

        i_recent_min = -1
        i_recent_max = -1
        i_recent_out = -1

        for i, num in enumerate(nums):

            if num < minK or num > maxK:
                i_recent_out = i

            if num == minK:
                i_recent_min = i

            if num == maxK:
                i_recent_max = i

            ans += max(0, min(i_recent_min, i_recent_max) - i_recent_out)

        return ans
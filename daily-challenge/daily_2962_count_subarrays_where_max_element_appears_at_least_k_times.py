"""
Find maximum element num by max of the given array
Sliding window

"""

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        ans = 0
        left = 0
        count = 0

        for right in range(len(nums)):
            if nums[right] == max_num:
                count += 1

            while count == k:
                if nums[left] == max_num:
                    count -= 1
                left += 1

            # By the amount left moved, we had subarrays that has at least k max_num
            ans += left

        return ans

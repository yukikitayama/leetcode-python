from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                k -= 1

            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
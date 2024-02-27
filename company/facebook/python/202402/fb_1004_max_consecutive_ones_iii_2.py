from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Edge
        if sum(nums) == 0:
            return k

        left = 0
        ans = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                k -= 1

            while left < right and k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans

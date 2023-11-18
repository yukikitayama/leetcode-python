from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()

        left = 0
        curr = 0
        ans = 0

        for right in range(len(nums)):

            target = nums[right]
            curr += target

            # Shrink
            while (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1

            # Max frequency is max length in sorted array
            ans = max(ans, right - left + 1)

        return ans

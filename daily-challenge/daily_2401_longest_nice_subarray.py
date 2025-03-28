from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 0
        used_bits = 0
        left = 0

        for right in range(len(nums)):

            # used_bits & nums[right] != 0 means some bits are overlapped
            while used_bits & nums[right] != 0:
                # 0 | 1 = 1
                # 1 ^ 1 = 0
                used_bits ^= nums[left]
                left += 1

            used_bits |= nums[right]

            ans = max(ans, right - left + 1)

        return ans
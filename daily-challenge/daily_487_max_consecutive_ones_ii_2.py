from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        r = 0
        zero_count = 0
        while r < len(nums):

            if nums[r] == 0:
                zero_count += 1

            while zero_count == 2:

                if nums[l] == 0:
                    zero_count -= 1

                l += 1

            ans = max(ans, r - l + 1)

            r += 1

        return ans


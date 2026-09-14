from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        l = nums[i]
        r = nums[j]
        ans = 0

        while i < j:

            if l < r:
                i += 1
                l += nums[i]
                ans += 1

            elif l > r:
                j -= 1
                r += nums[j]
                ans += 1

            else:
                i += 1
                l += nums[i]
                j -= 1
                r += nums[j]

        return ans

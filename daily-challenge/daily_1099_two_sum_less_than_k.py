from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        nums.sort()

        ans = -1

        left = 0
        right = len(nums) - 1

        while left < right:
            sum_ = nums[left] + nums[right]

            if sum_ < k:
                ans = max(ans, sum_)
                left += 1
            else:
                right -= 1

        return ans

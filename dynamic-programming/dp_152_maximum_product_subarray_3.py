"""
Start from brute force...
"""


from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        ans = nums[0]

        for i in range(len(nums)):
            accumulator = 1
            for j in range(i, len(nums)):
                accumulator *= nums[j]
                ans = max(ans, accumulator)

        return ans


nums = [2,3,-2,4]
nums = [-2,0,-1]
print(Solution().maxProduct(nums))

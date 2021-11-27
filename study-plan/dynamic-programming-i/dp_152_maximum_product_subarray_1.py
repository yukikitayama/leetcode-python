from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        result = float('-inf')

        for i in range(len(nums)):
            accumulated = 1
            for j in range(i, len(nums)):
                accumulated *= nums[j]
                result = max(result, accumulated)

        return result


"""
Brute force, TLE
"""


nums = [2, 3, -2, 4]
# nums = [-2,0,-1]
nums = [0, 2]
print(Solution().maxProduct(nums))

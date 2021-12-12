"""
- brute force
  - Get sum of nums
  - Get the half of the sum
  - Iterate each num in nums
    - Decide whether it should include the current num or not to form the half
  - Time is O(2^n)
- Top-down DP memoization
"""


from typing import List
import functools


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        @functools.lru_cache(maxsize=None)
        def recursion(nums, n, subset_sum):
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False

            result = (
                # Include next num to half sum
                recursion(nums, n - 1, subset_sum - nums[n - 1])
                # Or don't include the next num to half sum
                or recursion(nums, n - 1, subset_sum)
            )

            return result

        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        half_sum = total_sum // 2
        n = len(nums)

        return recursion(tuple(nums), n - 1, half_sum)


nums = [1,5,11,5]
nums = [1,2,3,5]
print(Solution().canPartition(nums))


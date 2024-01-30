"""
"""


from typing import List
import functools


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(i, left):

            # Base case
            if i == len(multipliers):
                return 0

            # Compute right index
            # e.g. i: 2, left: 1, right should be len(nums) - 1 - 1
            right = len(nums) - 1 - (i - left)

            return max(
                nums[left] * multipliers[i] + dp(i + 1, left + 1),
                nums[right] * multipliers[i] + dp(i + 1, left)
            )

        return dp(0, 0)


if __name__ == "__main__":
    nums = [1, 2, 3]
    multipliers = [3, 2, 1]
    # 14

    nums = [-5, -3, -3, -2, 7, 1]
    multipliers = [-10, -5, 3, 4, 6]
    # 102

    print(Solution().maximumScore(nums, multipliers))

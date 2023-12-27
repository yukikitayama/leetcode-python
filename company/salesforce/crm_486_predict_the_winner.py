"""
Recursion, O(2 ** n) time
"""

from typing import List
import functools


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        @functools.lru_cache(maxsize=None)
        def recursion(left, right):
            if left == right:
                return nums[left]

            return max(
                # Player 1 score minus Player 2 score
                nums[left] - recursion(left + 1, right),
                nums[right] - recursion(left, right - 1)
            )

        return recursion(0, len(nums) - 1) >= 0


if __name__ == "__main__":
    nums = [1, 5, 2]  # F
    nums = [1, 5, 233, 7]  # T
    print(Solution().predictTheWinner(nums))

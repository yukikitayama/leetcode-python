"""
find key indices
"""

from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        right = 0
        for center in range(len(nums)):

            if nums[center] == key:

                left = max(
                    right,
                    center - k
                )

                right = min(
                    len(nums) - 1,
                    center + k
                ) + 1

                for i in range(left, right):
                    ans.append(i)

        return ans
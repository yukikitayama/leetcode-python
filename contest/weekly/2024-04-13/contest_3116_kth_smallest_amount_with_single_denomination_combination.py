"""
Binary search
https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/solutions/5019504/python3-math-inclusion-exclusion-principle-binary-search/
"""

from typing import List


class Solution:

    def findKthSmallest1(self, coins: List[int], k: int) -> int:
        """Memory limit exceeded"""
        nums_set = set()
        for i in range(len(coins)):
            for j in range(1, k + 1):
                nums_set.add(coins[i] * j)

        nums_list = list(nums_set)
        nums_list.sort()

        return nums_list[k - 1]
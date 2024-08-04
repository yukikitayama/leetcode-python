"""
The first element of nums always corresponds to the root node of the corresponding BST.
Let dfs(nums) denote the number of permutations of nums that result in the same BST as nums
As long as the relative position of the elements within [1, 2] or [4, 5] remains unchanged, rearranging their positions in nums does not affect the construction of the subtrees


4C2 = 4 * 3 * 2 / (2 * 2) = 24 / 4 = 6
"""

from typing import List
import math


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        def dfs(nums):
            # Terminate
            if len(nums) <= 2:
                return 1

            left_nodes = [num for num in nums if num < nums[0]]
            right_nodes = [num for num in nums if num > nums[0]]

            # -1 because leftmost num is fixed
            return math.comb(len(nums) - 1, len(left_nodes)) * dfs(left_nodes) * dfs(right_nodes) % MOD

        # -1 because the original nums is not included in the number of valid permutations
        return (dfs(nums) - 1) % MOD

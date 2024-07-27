"""
We should use bigger greatest common divisor later to maximize score.

As integers have 32 bits, each bit can be 0 or 1. We can use these bits to represent if an element of our array is picked or not.
In an integer number (say mask) if the bit at position i is 0, it means the array element at the i
th
  index is not picked otherwise if it's 1 it means the element was picked earlier.
"""

from typing import List
import math


class Solution:
    def maxScore(self, nums: List[int]) -> int:

        memo = {}

        def dp(mask, pairs_picked):

            # Base case: No more numbers, no more addition of GCD
            if 2 * pairs_picked == len(nums):
                return 0

            # Return memoized value
            if mask in memo:
                return memo[mask]

            res = 0

            for left in range(len(nums)):
                for right in range(left + 1, len(nums)):

                    # If already chose either index, skip
                    if (mask >> left) & 1 == 1 or (mask >> right) & 1 == 1:
                        continue

                    new_mask = mask | (1 << left)
                    new_mask |= (1 << right)

                    curr_score = (pairs_picked + 1) * math.gcd(nums[left], nums[right])

                    remaining_score = dp(new_mask, pairs_picked + 1)

                    res = max(res, curr_score + remaining_score)

            memo[mask] = res
            return memo[mask]

        return dp(mask=0, pairs_picked=0)

"""
Ans
  How many arrays of length n with values in the range [1, m] exist, such that
  you will find exactly k new maximums when iterating from left to right?
  seach_cost = 0; search_cost = search_cost + 1;
  is just incrementing search_cost every time we see a new max, so
  it means just counting a new max
"""

import functools


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:

        MOD = 10 ** 9 + 7

        @functools.cache
        def dp(i, max_so_far, remain_num_max):

            # Base: get n elements
            if i == n:
                # found a target array
                if remain_num_max == 0:
                    return 1
                # Counldn't find k new max
                else:
                    return 0

            # Base: Found too many new max before reaching n
            if remain_num_max < 0:
                return 0

            # Case 1: Don't place a new max
            # We have [1, max_so_far] otions of numbers to avoid updating new max
            # max_so_far - 1 + 1 (+1 for both ends to be inclusive)
            # We multiply because if the next number can correctly terminate the recursion
            # , meaning returning 1, we have max_so_far choices to diversify it
            ans = (max_so_far * dp(i + 1, max_so_far, remain_num_max)) % MOD

            # Case 2: Place a number that is a new max
            # m + 1 because m is a usable number
            for new_max in range(max_so_far + 1, m + 1):
                # Go to next number with this new max and seeing one new max
                ans = (ans + dp(i + 1, new_max, remain_num_max - 1)) % MOD

            return ans

        return dp(0, 0, k)

"""
Create counter for each binary string
for each counter, check m and n counts
Brute fource
(strs[i] length * strs length) + strs length
"""

from typing import List
import functools
import collections


class Solution:
    # def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    #     idx_to_counter = collections.defaultdict(collections.Counter)
    #     for i in range(len(strs)):
    #         counter = collections.Counter(strs[i])
    #         idx_to_counter[i] = counter

    #     # Base case is 0
    #     dp = [[0] * (n + 1) for _ in range(m + 1)]

    #     for i in range(len(strs)):
    #         curr_zero = idx_to_counter[i]["0"]
    #         curr_one = idx_to_counter[i]["1"]

    #         for zero in range(m, -1, -1):
    #             for one in range(n, -1, -1):
    #                 if zero - curr_zero >= 0 and one - curr_one >= 0:
    #                     dp[zero][one] = max(
    #                         dp[zero][one],
    #                         1 + dp[zero - curr_zero][one - curr_one]
    #                     )

    #         return dp[m][n]

    def findMaxForm1(self, strs: List[str], m: int, n: int) -> int:

        idx_to_counter = collections.defaultdict(collections.Counter)
        for i in range(len(strs)):
            counter = collections.Counter(strs[i])
            idx_to_counter[i] = counter

        # print(idx_to_counter)

        @functools.cache
        def dp(index, zero, one):

            # Base case
            if index == len(strs):
                return 0

            curr_zero = idx_to_counter[index]["0"]
            curr_one = idx_to_counter[index]["1"]

            res = float("-inf")

            # Include current string
            if zero - curr_zero >= 0 and one - curr_one >= 0:
                res = max(
                    res,
                    # +1 to include current string to subset
                    1 + dp(index + 1, zero - curr_zero, one - curr_one)
                )

            # Or skip current string
            res = max(
                res,
                dp(index + 1, zero, one)
            )

            return res

        return dp(0, m, n)
"""
dp(i)
  returns minimum dollars to travel first ith days array
"""

from typing import List
import functools


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)

        i = 0
        for day in range(1, days[-1] + 1):

            if day < days[i]:
                dp[day] = dp[day - 1]

            else:
                dp[day] = min(
                    dp[day - 1] + costs[0],
                    dp[max(day - 7, 0)] + costs[1],
                    dp[max(day - 30, 0)] + costs[2]
                )
                i += 1

        return dp[-1]

    def mincostTickets1(self, days: List[int], costs: List[int]) -> int:

        days_set = set(days)

        @functools.cache
        def dp(curr_day):

            # Base case
            if curr_day > days[-1]:
                return 0

            if curr_day not in days_set:
                return dp(curr_day + 1)

            else:
                return min(
                    costs[0] + dp(curr_day + 1),
                    costs[1] + dp(curr_day + 7),
                    costs[2] + dp(curr_day + 30)
                )

        return dp(1)
"""
backtracking?
"""

from typing import List
import functools


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        is_travel_needed = set(days)

        @functools.lru_cache(maxsize=None)
        def dp(curr_day):

            # If travel finished, no more to spend cost
            if curr_day > days[-1]:
                return 0

            # If current day isn't in days to travel, skip this day and go to the next day
            if curr_day not in is_travel_needed:
                return dp(curr_day + 1)

            one_day_cost = costs[0] + dp(curr_day + 1)
            seven_day_cost = costs[1] + dp(curr_day + 7)
            thirty_day_cost = costs[2] + dp(curr_day + 30)

            return min(one_day_cost, seven_day_cost, thirty_day_cost)

        return dp(1)

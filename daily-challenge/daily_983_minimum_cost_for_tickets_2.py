from typing import List
import functools


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        days_set = set(days)

        @functools.cache
        def dp(day):

            # Base: No more travel needed
            if day > days[-1]:
                return 0

            # Recurrence: skip current day and go to next
            if day not in days_set:
                return dp(day + 1)

            # Recurrence: travel current day
            one = costs[0] + dp(day + 1)
            seven = costs[1] + dp(day + 7)
            thirty = costs[2] + dp(day + 30)

            return min(one, seven, thirty)

        return dp(1)
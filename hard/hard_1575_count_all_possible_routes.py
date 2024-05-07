"""
DFS
  each visit decements fuel
  fuel cannot be negative
"""

from typing import List
import functools


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(curr_city, remaining_fuel):

            # Base
            if remaining_fuel < 0:
                return 0

            # State transition
            ans = 0

            if curr_city == finish:
                ans = 1

            for next_city in range(len(locations)):

                if curr_city != next_city:
                    next_fuel = remaining_fuel - abs(locations[curr_city] - locations[next_city])

                    ans = (ans + dp(next_city, next_fuel)) % (10 ** 9 + 7)

            return ans

        return dp(start, fuel)
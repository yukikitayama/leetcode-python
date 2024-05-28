"""
Sort events by start date
"""

from typing import List
import bisect
import functools


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """Bottom-up DP"""
        events.sort(key=lambda x: x[0])
        starts = [start for start, end, value in events]

        dp = [[0] * (k + 1) for _ in range(len(events) + 1)]

        for curr_i in range(len(events) - 1, -1, -1):
            for remaining in range(1, k + 1):
                next_i = bisect.bisect_right(starts, events[curr_i][1])

                dp[curr_i][remaining] = max(
                    # Attend current event
                    events[curr_i][2] + dp[next_i][remaining - 1],
                    # Skip current event (So transfer previous value)
                    dp[curr_i + 1][remaining]
                )

        # for row in dp:
        #     print(row)

        return dp[0][k]

    def maxValue1(self, events: List[List[int]], k: int) -> int:
        """Top-down DP"""

        events.sort(key=lambda x: x[0])
        starts = [start for start, end, value in events]

        @functools.cache
        def dp(index, remaining):

            # Base case
            if index == len(events):
                return 0
            if remaining == 0:
                return 0

            # Find index of next event if attend current event
            next_index = bisect.bisect_right(starts, events[index][1])

            return max(
                # Attend current event
                events[index][2] + dp(next_index, remaining - 1),
                # Or skip current event
                dp(index + 1, remaining)
            )

        return dp(0, k)
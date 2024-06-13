"""
n = 5, ranges = [3,4,1,1,0,0]
i: 2, ranges[2]: 1, tap_start: 2 - 1 = 1, tap_end: 2 + 1 = 3
"""

from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        dp = [float("inf")] * (n + 1)

        # Base case: no need to open any taps to water zero length garden
        dp[0] = 0

        for i in range(n + 1):
            tap_start = max(0, i - ranges[i])
            tap_end = min(n, ranges[i] + i)

            for j in range(tap_start, tap_end + 1):
                dp[tap_end] = min(
                    # Previous tap can already water current tap_end
                    dp[tap_end],
                    # Or more previous tap plus curret tap can cover current tap_end
                    dp[j] + 1
                )

        return dp[-1] if dp[-1] != float("inf") else -1

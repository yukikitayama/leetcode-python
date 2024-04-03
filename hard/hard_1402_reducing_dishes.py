"""
We wanna make earlier the dish which has low satisfaction
We wanna make later the dish which has high satisfaction

Sort satisfaction in ascending order
and DP?

[-1, -8, 0, 5, -9]
Sorting
[-9, -8, -1, 0, 5]
We choose to make current dish or skip
i: 0
  -9 * 1, next time: 2
  or 0, next time stays 1
i: 1

DP matrix
  (i, t)
    i: ith dish
    t: time to make current dish
      1 to length of satisfaction array
  dp[i][t] = dp[i - 1][t - 1] + satisfaction[i] * t
"""

from typing import List
import functools


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """Bottom-up DP
        dp[i][t] represents the max sum satisfaction by making current dish i with time t
        """
        satisfaction.sort()
        # +2 because t is 1-based index and need extra one to have the below nested for-loop can work for all the cases
        # +1 for all the nested for-loop can work without extra conditions
        dp = [[0] * (len(satisfaction) + 2) for _ in range(len(satisfaction) + 1)]

        for i in range(len(satisfaction) - 1, -1, -1):
            for t in range(1, len(satisfaction) + 1):
                dp[i][t] = max(
                    # Create current dish and go to next dish
                    satisfaction[i] * t + dp[i + 1][t + 1],
                    # Or skip current dish and go to next dish
                    dp[i + 1][t]
                )

        # for row in dp:
        #     print(row)

        return dp[0][1]

    def maxSatisfaction2(self, satisfaction: List[int]) -> int:
        """Top-down DP"""
        satisfaction.sort()

        @functools.lru_cache(maxsize=None)
        def dp(i, t):
            # Terminate: No more dish to create, no more satisfaction to add
            if i == len(satisfaction):
                return 0

            return max(
                # Create current dish and go to next dish
                satisfaction[i] * t + dp(i + 1, t + 1),
                # Or skip current dish and go to next dish
                dp(i + 1, t)
            )

        return dp(0, 1)

    def maxSatisfaction1(self, satisfaction: List[int]) -> int:
        """First attempt"""
        satisfaction.sort()

        dp = [[0] * (len(satisfaction) + 1) for _ in range(len(satisfaction))]

        # Base
        for i in range(len(satisfaction)):
            dp[i][1] = satisfaction[i] * 1

        ans = float("-inf")

        t = 2
        for t in range(2, len(satisfaction) + 1):
            for i in range(1, len(satisfaction)):
                # Create current dish after making previou dish
                dp[i][t] = dp[i - 1][t - 1] + satisfaction[i] * t

                max_satisfaction = max(dp[i])
                ans = max(ans, max_satisfaction)

        # for row in dp:
        #     print(row)

        return 0 if ans == float("-inf") else ans
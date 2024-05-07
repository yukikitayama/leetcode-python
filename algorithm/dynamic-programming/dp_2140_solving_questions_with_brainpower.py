"""
dp(index of questions, bool)
"""

from typing import List
import functools


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)

        # Base
        dp[-1] = questions[-1][0]

        # State transition
        for i in range(len(questions) - 2, -1, -1):

            dp[i] = questions[i][0]

            if i + questions[i][1] + 1 < len(questions):
                dp[i] += dp[i + questions[i][1] + 1]

            # Solve ith question or skip
            dp[i] = max(dp[i], dp[i + 1])

        return dp[0]

    def mostPoints1(self, questions: List[List[int]]) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(i):
            # Base case: No points from no question
            if i >= len(questions):
                return 0

            # State transition: Solve current question and skip, or skip current question to next
            return max(
                questions[i][0] + dp(i + questions[i][1] + 1),
                dp(i + 1)
            )

        return dp(0)
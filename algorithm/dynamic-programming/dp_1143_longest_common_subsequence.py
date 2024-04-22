import functools


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # Use shorter text for DP
        if len(text2) < len(text1):
            text1, text2 = text2, text1

        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text1) + 1)

        for col in range(len(text2) - 1, -1, -1):
            for row in range(len(text1) - 1, -1, -1):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(
                        previous[row],
                        current[row + 1]
                    )

            previous, current = current, previous

        return previous[0]

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for col in range(len(text2) - 1, -1, -1):
            for row in range(len(text1) - 1, -1, -1):
                if text2[col] == text1[row]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(
                        dp[row + 1][col],
                        dp[row][col + 1]
                    )

        return dp[0][0]

    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:

        @functools.cache
        def dp(p1, p2):

            # Terminate
            if p1 < 0 or p2 < 0:
                return 0

            if text1[p1] == text2[p2]:
                return 1 + dp(p1 - 1, p2 - 1)
            else:
                return max(
                    dp(p1 - 1, p2),
                    dp(p1, p2 - 1)
                )

        return dp(len(text1) - 1, len(text2) - 1)
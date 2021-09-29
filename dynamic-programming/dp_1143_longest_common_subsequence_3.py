"""
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):

                if text2[col] == text1[row]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]

                else:
                    dp[row][col] = max(
                        dp[row + 1][col],
                        dp[row][col + 1]
                    )
        return dp[0][0]


"""
Bottom up dynamic programming
"""


text1 = "abcde"
text2 = "ace"
print(Solution().longestCommonSubsequence(text1, text2))

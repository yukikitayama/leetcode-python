"""
- dp[i][j] represents the length of longest common sequence up to i index in text1 and j index in text2
- return dp[-1][-1]
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # In dp matrix, row is text1 and col is text2

        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

        # print('dp')
        # [print(row) for row in dp]

        return dp[-1][-1]


text1 = "abcde"
text2 = "ace"
text1 = "abc"
text2 = "abc"
text1 = "abc"
text2 = "def"
print(Solution().longestCommonSubsequence(text1, text2))

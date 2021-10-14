"""
- 2d dp array
  - row text1 + 1, col text2 + 1
  - if match, dp[i][j] = dp[i - 1][j - 1] + 1
  - else, dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
  - dp[i][j] represents the length of the longest common subsequence so far
"""


from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):

            # Base case
            # If either string is empty no match
            if p1 == len(text1) or p2 == len(text2):
                return 0

            # Option 1
            # Don't include text1[p1]
            option_1 = memo_solve(p1 + 1, p2)

            # Option 2
            # Include test1[p1]
            first_occurence = text2.find(text1[p1], p2)
            # But we still could not find the character, so initialize with 0
            option_2 = 0
            if first_occurence != -1:
                option_2 = 1 + memo_solve(p1 + 1, first_occurence + 1)

            return max(option_1, option_2)

        return memo_solve(0, 0)


"""
Top down dynamic programming
"""


text1 = "abcde"
text2 = "ace"
print(Solution().longestCommonSubsequence(text1, text2))

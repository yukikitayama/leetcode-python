"""
Top down DP
  dp(p1, p2)
    base case
      if p1 and p2 less than 0
        return 0
    if current characters are same
      dp(p1 - 1, p2 - 1)
    if current characters are not the same
      get minimum of followings
      dp(p1 - 1, p2)
        Delete a character from word1
      dp(p1, p2 - 1)
        Insert a character to word1
      dp(p1 - 1, -2 - 1)
        Replace a character
"""

import functools


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Bottom-up"""
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for r in range(len(word1)):
            dp[r + 1][0] = r + 1

        for c in range(len(word2)):
            dp[0][c + 1] = c + 1

        for p1 in range(len(word1)):
            for p2 in range(len(word2)):

                if word1[p1] == word2[p2]:
                    dp[p1 + 1][p2 + 1] = dp[p1][p2]

                else:
                    dp[p1 + 1][p2 + 1] = 1 + min(
                        dp[p1][p2 + 1],
                        dp[p1 + 1][p2],
                        dp[p1][p2]
                    )

        # for row in dp:
        #     print(row)

        return dp[-1][-1]

    def minDistance1(self, word1: str, word2: str) -> int:
        """Top-down"""

        @functools.lru_cache(maxsize=None)
        def dp(p1, p2):
            if p1 < 0:
                # No more word1 characters, so insert
                # +1 because p2 is 0-based index, if p2 is 0, we need to insert 1 character
                return p2 + 1
            elif p2 < 0:
                # No characters left in word2, so we need to delete word1 characters
                # +1 because p1 is 0-based index, if p1 is 0, we need to delete 1 character
                return p1 + 1

            if word1[p1] == word2[p2]:
                return dp(p1 - 1, p2 - 1)
            elif word1[p1] != word2[p2]:
                return 1 + min(
                    dp(p1 - 1, p2),
                    dp(p1, p2 - 1),
                    dp(p1 - 1, p2 - 1)
                )

        return dp(len(word1) - 1, len(word2) - 1)

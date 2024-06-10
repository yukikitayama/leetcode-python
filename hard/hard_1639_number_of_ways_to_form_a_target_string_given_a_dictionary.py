from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7

        char_occurrences = [[0] * len(words[0]) for _ in range(26)]
        for i in range(len(words)):
            for j in range(len(words[i])):
                char_occurrences[ord(words[i][j]) - ord("a")][j] += 1

        for row in char_occurrences:
            print(row)

        dp = [[0] * (len(words[0]) + 1) for _ in range(len(target) + 1)]

        # Base case: one way to create empty without using column
        dp[0][0] = 1

        # State transition
        for r in range(len(dp)):
            for c in range(len(dp[0]) - 1):

                # Include current character
                if r < len(target):
                    dp[r + 1][c + 1] += char_occurrences[ord(target[r]) - ord("a")][c] * dp[r][c]
                    dp[r + 1][c + 1] %= MOD

                # Skip current character
                dp[r][c + 1] += dp[r][c]
                dp[r][c + 1] %= MOD

        return dp[-1][-1]
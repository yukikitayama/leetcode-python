"""
- Find the length of the longest common subsequence
- Answer is m + n - (2 * longest common subsequence)
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = max(
                    dp[i][j + 1],
                    dp[i + 1][j],
                    dp[i][j] + (word1[i] == word2[j])
                )

        return m + n - (2 * dp[m][n])


if __name__ == '__main__':
    word1 = "sea"
    word2 = "eat"
    # 2
    word1 = "leetcode"
    word2 = "etco"
    # 4
    print(Solution().minDistance(word1, word2))

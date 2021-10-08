class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        # Id one of the string is empty
        if n * m == 0:
            # n + m because if either is empty, we don't know which is empty
            # so n + m is n + 0 or 0 + m, and it successfully returns the edit distance
            return n + m

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Base case
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j

        # DP compute
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # If the previous character is the same,
                # Append one character to a word whose length is one less than the other word,
                # or

                # -1 to i and j because dp array is one length longer than word1 and word2
                # so even if -1, in word1 and word2, it looks at the current character in word1 and word2
                # so the if conditions means that if the current characters in word1 and word2 are the same
                if word1[i - 1] == word2[j - 1]:
                    # dp[i - 1][j] and dp[i][j - 1] refers the different length of words, so need to +1
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])

                # if the current character from word1 and word2 are different
                elif word1[i - 1] != word2[j - 1]:
                    # dp[i - 1][j - 1] + 1 because current characters are different so do one delete operation
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

        return dp[n][m]


word1 = "horse"
word2 = "ros"
# word1 = "intention"
# word2 = "execution"
print(Solution().minDistance(word1, word2))



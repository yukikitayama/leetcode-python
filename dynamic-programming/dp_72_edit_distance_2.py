"""

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case
        for row in range(len(dp)):
            dp[row][0] = row
        for col in range(len(dp[0])):
            dp[0][col] = col

        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):

                # if current word is the same, there's no need to do any operations of
                # inserting, deleting or replaceing, so we don't add length
                # -1 for word1 and word2 because word1 and word2 are one length smaller than dp matrix
                if word1[row - 1] == word2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1]

                # Otherwise we need to do one of the operations, so add one to the previous state
                # But we wanna find minimum number of operations, so out of three choices, take min
                else:
                    dp[row][col] = 1 + min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1])

        # The answer is at the end of that's considered all the characters in both words
        return dp[-1][-1]


word1 = "horse"
word2 = "ros"
word1 = "intention"
word2 = "execution"
print(Solution().minDistance(word1, word2))

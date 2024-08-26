"""
Dynamic programming
"""


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        n = len(s1)

        dp = []
        # Length of section
        for l in range(n + 1):
            is_ = []
            # Start of section for s1
            for i in range(n):
                js = []
                # Start of section for s2
                for j in range(n):
                    js.append(False)
                is_.append(js)
            dp.append(is_)

        # Base case: 1 characters and both are the same character
        # s1 index
        for i in range(n):
            # s2 index
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]

        # 2 because length 1 checked in base case
        for length in range(2, n + 1):
            # One part for s1
            for i in range(n + 1 - length):
                # One part for s2
                for j in range(n + 1 - length):
                    # The other part
                    for new_length in range(1, length):
                        # Left
                        dp1 = dp[new_length][i]
                        # Right
                        dp2 = dp[length - new_length][i + new_length]

                        dp[length][i][j] |= dp1[j] and dp2[j + new_length]

                        # Swap
                        dp[length][i][j] |= dp1[j + length - new_length] and dp2[j]

        # print(dp)

        return dp[n][0][0]
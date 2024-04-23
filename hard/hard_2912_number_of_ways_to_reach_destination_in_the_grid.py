"""
DFS

Ans
  dp
"""

from typing import List


class Solution:
    def numberOfWays(self, n: int, m: int, k: int, source: List[int], dest: List[int]) -> int:

        MOD = 10 ** 9 + 7

        # dp[i][0]: Number of ways to destination with i steps
        # dp[i][1]: Number of ways to get to same rows as destination with i steps
        # dp[i][2]: Number of ways to get to same columns as destination with i steps
        # dp[i][3]: Number of ways to get to the else places with i steps
        dp = [[0] * 4 for _ in range(k + 1)]

        # Base cases

        if source == dest:
            dp[0][0] = 1

        # Row
        elif source[0] == dest[0]:
            dp[0][1] = 1

        # Column
        elif source[1] == dest[1]:
            dp[0][2] = 1

        else:
            dp[0][3] = 1

        # print(f"i: {0}")
        # for row in dp:
        #     print(row)
        # print()

        # State transition, recurrence relationship
        for i in range(1, k + 1):
            # To be the same row and column, previously need to be either same row or same column
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % MOD

            # To be the same row,
            dp[i][1] = (
                           # (m - 1) to remove self
                               dp[i - 1][0] * (m - 1)
                               # (m - 2) to remove and target
                               + dp[i - 1][1] * (m - 2)
                               # You can come to same row state directly from else state by either move row-wise or move column-wise
                               + dp[i - 1][3]
                       ) % MOD

            # To be the same column
            dp[i][2] = (
                           # (n - 1) to remove self
                               dp[i - 1][0] * (n - 1)
                               # (n - 2) to remove self and target
                               + dp[i - 1][2] * (n - 2)
                               # You can come to same row state directly from else state by either move row-wise or move column-wise
                               + dp[i - 1][3]
                       ) % MOD

            # To be elsewhere
            dp[i][3] = (
                           # Doesn't have dp[i - 1][0] because you need to have 2 steps

                           # (n - 1) to remove self
                               dp[i - 1][1] * (n - 1)
                               # (m - 1) to remove self
                               + dp[i - 1][2] * (m - 1)
                               # m + n because m choice to come here vertical move, n choices to come here horizontal move
                               # but we remove self, same row, same column, target
                               + dp[i - 1][3] * (m + n - 4)
                       ) % MOD

            # print(f"i: {i}")
            # for row in dp:
            #     print(row)
            # print()

        return dp[k][0]
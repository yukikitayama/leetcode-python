from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10 ** 9 + 7

        apples = [[0] * (len(pizza[0]) + 1) for _ in range(len(pizza) + 1)]

        for r in range(len(pizza) - 1, -1, -1):
            for c in range(len(pizza[0]) - 1, -1, -1):
                apples[r][c] = (
                        int(pizza[r][c] == "A")
                        + apples[r + 1][c]
                        + apples[r][c + 1]
                        # Subtract overlapping from the above two
                        - apples[r + 1][c + 1]
                )

        # for row in apples:
        #     print(row)

        dp = [[[0] * len(pizza[0]) for _ in range(len(pizza))] for _ in range(k)]

        # Base case: no more cut, whether the current pizza cut contains at least one apple
        dp[0] = [[int(apples[r][c] > 0) for c in range(len(pizza[0]))] for r in range(len(pizza))]

        # print(dp[0])

        for remaining_cut in range(1, k):
            for r in range(len(pizza)):
                for c in range(len(pizza[0])):
                    ways = 0

                    for next_r in range(r + 1, len(pizza)):

                        # If at least one apple
                        if apples[r][c] - apples[next_r][c] > 0:
                            ways += dp[remaining_cut - 1][next_r][c]

                    for next_c in range(c + 1, len(pizza[0])):

                        # If at least one apple
                        if apples[r][c] - apples[r][next_c] > 0:
                            ways += dp[remaining_cut - 1][r][next_c]

                    dp[remaining_cut][r][c] = ways % MOD

        return dp[k - 1][0][0]

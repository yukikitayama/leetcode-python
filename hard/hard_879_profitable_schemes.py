from typing import List
import functools


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        MOD = 10 ** 9 + 7
        # dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(len(group) + 1)]

        # print(len(dp), len(dp[0]), len(dp[0][0]))

        # Base case: Consider all the crimes, as long as number of members <= n, and achieve minProfit
        for i in range(n + 1):
            dp[len(group)][i][minProfit] = 1

        # State transition
        for index in range(len(group) - 1, -1, -1):
            for num_member in range(n + 1):
                for curr_profit in range(minProfit + 1):

                    # Skip crime
                    dp[index][num_member][curr_profit] = dp[index + 1][num_member][curr_profit]

                    # Commit crime
                    if num_member + group[index] <= n:
                        dp[index][num_member][curr_profit] = (
                                                                     dp[index][num_member][curr_profit]
                                                                     + dp[index + 1][num_member + group[index]][
                                                                         min(minProfit, curr_profit + profit[index])]
                                                             ) % MOD

        return dp[0][0][0]

    def profitableSchemes1(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        MOD = 10 ** 9 + 7

        @functools.cache
        def dp(index, num_member, curr_profit):

            # Base case
            if index == len(group):
                if curr_profit == minProfit:
                    return 1
                else:
                    return 0

            ans = 0

            # Commit current crime
            if num_member + group[index] <= n:
                # min() reduces the number of states for DP
                # We just want at least minProfit when counting the variety of commit crime or skip crime, so we don't care the amount of actual profit made as long as it exceeds minProfit
                ans = (ans + dp(index + 1, num_member + group[index],
                                min(minProfit, curr_profit + profit[index]))) % MOD

            # Skip current crime
            ans = (ans + dp(index + 1, num_member, curr_profit)) % MOD

            return ans

        return dp(0, 0, 0)
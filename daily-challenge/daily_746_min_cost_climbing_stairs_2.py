"""
- top down DP
"""


from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two_step_before = 0
        one_step_before = 0

        for i in range(2, len(cost) + 1):
            two_step_before = two_step_before + cost[i - 2]
            one_step_before = one_step_before + cost[i - 1]
            ans = min(two_step_before, one_step_before)


        return ans


class Solution3:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {
            0: 0,
            1: 0
        }

        def dp(i):
            if i in memo:
                return memo[i]

            memo[i] = min(dp(i - 2) + cost[i - 2], dp(i - 1) + cost[i - 1])

            return memo[i]

        dp(len(cost))
        return memo[len(cost)]


class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)

        for i in range(2, len(dp)):
            dp[i] = min(cost[i - 2] + dp[i - 2], dp[i - 1] + cost[i - 1])

        return dp[-1]


class Solution1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float('inf')] * len(cost)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, len(cost)):

            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        # print(f'dp: {dp}')
        # print(f'{dp[-2] + cost[-2]}, {dp[-1] + cost[-1]}')

        return min(dp[-2] + cost[-2], dp[-1] + cost[-1])


if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    # 6
    # cost = [10, 15, 20]
    # 15
    print(Solution().minCostClimbingStairs(cost))

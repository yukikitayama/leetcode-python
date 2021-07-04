from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # +1 because we want to make one element longer
        minimum_cost = [0] * (len(cost) + 1)

        # +1 because range stop is exclusive
        for i in range(2, len(cost) + 1):
            take_one_step = minimum_cost[i - 1] + cost[i - 1]
            take_two_step = minimum_cost[i - 2] + cost[i - 2]
            minimum_cost[i] = min(take_one_step, take_two_step)

        return minimum_cost[-1]


cost = [10,15,20]
print(f'Answer: {Solution().minCostClimbingStairs(cost)}')

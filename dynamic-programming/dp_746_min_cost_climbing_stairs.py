from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minimum_cost = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            take_one_step = cost[i - 1] + minimum_cost[i - 1]
            take_two_step = cost[i - 2] + minimum_cost[i - 2]
            minimum_cost[i] = min(take_one_step, take_two_step)

        return minimum_cost[-1]


"""
For example, we have cost of steps by [10, 15, 20].
20 is not the top. 20 is the cost at the step by 1 step before the top.
From 20, we pay 20 to go to the top. We are allowed to make 1 or 2 steps.
So from 15, we only pay 15 and take 2 steps to reach the top, by skipping paying 20.

Bottom-up dynamic programming (Tabulation)
Time complexity
Let n be the length of cost. O(n) for for loop

Space complexity
O(n) for dp array
"""


cost = [1,100,1,1,1,100,1,1,100,1]
print(Solution().minCostClimbingStairs(cost))

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        down_one = down_two = 0

        for i in range(2, len(cost) + 1):
            curr_cost = min(down_one + cost[i - 1], down_two + cost[i - 2])
            down_two = down_one
            down_one = curr_cost
            # print(f'curr_cost: {curr_cost}')

            # tmp = down_one
            # down_one = min(down_one + cost[i - 1], down_two + cost[i - 2])
            # down_two = tmp

        return curr_cost
        # return down_one


"""
Time complexity
Let n be the length of cost
O(n) for for loop

Space complexity
We no longer have recursion call stack or memoization or dp array or dictionary
we only use constant variables, so O(1)
"""


cost = [1,100,1,1,1,100,1,1,100,1]
print(Solution().minCostClimbingStairs(cost))

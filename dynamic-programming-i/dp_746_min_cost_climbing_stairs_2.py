from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def minimum_cost(i):
            if i <= 1:
                return 0

            if i in memo:
                return memo[i]

            down_one = cost[i - 1] + minimum_cost(i - 1)
            down_two = cost[i - 2] + minimum_cost(i - 2)
            memo[i] = min(down_one, down_two)
            return memo[i]

        memo = {}
        return minimum_cost(len(cost))

"""
Time complexity
Let n be the length of cost
minimum_cost gets called n times to get memoization value for each step
O(n)

Space complexity
We use recursion function, so we need space for recursion call stack.
and we have length n hashmap
so O(n + n) = O(2n) = O(n)
"""


cost = [1,100,1,1,1,100,1,1,100,1]
print(Solution().minCostClimbingStairs(cost))

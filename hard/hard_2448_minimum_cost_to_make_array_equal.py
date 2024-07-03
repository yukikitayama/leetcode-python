from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        nums_and_cost = [[n, c] for n, c in zip(nums, cost)]
        nums_and_cost.sort()

        prefix_sum_cost = [nums_and_cost[0][1]]
        for i in range(1, len(nums_and_cost)):
            prefix_sum_cost.append(prefix_sum_cost[-1] + nums_and_cost[i][1])

        # print(nums_and_cost)
        # print(prefix_sum_cost)

        # Use first element as base case to initialize total cost
        total_cost = 0
        for i in range(1, len(nums_and_cost)):
            # cost * num diff
            total_cost += nums_and_cost[i][1] * (nums_and_cost[i][0] - nums_and_cost[0][0])

        # Initialize answer
        ans = total_cost

        # Try the rest of the elements as base
        for i in range(1, len(nums_and_cost)):
            diff = nums_and_cost[i][0] - nums_and_cost[i - 1][0]

            # Left part increases
            total_cost += prefix_sum_cost[i - 1] * diff

            # Right part decreases
            # -prefix_sum_cost[i - 1] to include current element
            # current element increases from the prev, so we reduce the total cost including current element
            total_cost -= (prefix_sum_cost[-1] - prefix_sum_cost[i - 1]) * diff

            ans = min(ans, total_cost)

        return ans
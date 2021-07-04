from typing import List

class Solution:
    def __init__(self):
        self.memo = None
        self.costs = None

    def minCost(self, costs: List[List[int]]) -> int:

        self.costs = costs

        if not costs:
            return 0

        # Key: (nth row, color index), Value: total_cost
        self.memo = {}

        return min(self.paint_cost(0, 0), self.paint_cost(0, 1), self.paint_cost(0, 2))

    def paint_cost(self, n: int, color: int) -> int:
        if (n, color) in self.memo:
            return self.memo[(n, color)]

        total_cost = self.costs[n][color]

        # This case is to reach bottom of the tree, so it should record total cost and return it
        if n == len(self.costs) - 1:
            pass

        elif color == 0:
            total_cost += min(self.paint_cost(n + 1, 1), self.paint_cost(n + 1, 2))
        elif color == 1:
            total_cost += min(self.paint_cost(n + 1, 0), self.paint_cost(n + 1, 2))
        else:
            total_cost += min(self.paint_cost(n + 1, 0), self.paint_cost(n + 1, 1))

        self.memo[(n, color)] = total_cost

        return total_cost


costs = [[17,2,17],[16,16,5],[14,3,19]]
print(f'Answer: {Solution().minCost(costs)}')

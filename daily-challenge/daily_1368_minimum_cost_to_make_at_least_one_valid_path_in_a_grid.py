from typing import List
import heapq


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:

        # [(cost, row, col), ...]
        min_heap = [(0, 0, 0)]
        min_cost = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]
        min_cost[0][0] = 0

        while min_heap:

            cost, row, col = heapq.heappop(min_heap)

            # 1: right, 2: left, 3: lower, 4: upper
            for i, (dr, dc) in enumerate([(0, 1), (0, -1), (1, 0), (-1, 0)]):
                new_row = row + dr
                new_col = col + dc

                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):

                    direction = i + 1
                    if direction != grid[row][col]:
                        new_cost = cost + 1
                    else:
                        new_cost = cost

                    if min_cost[new_row][new_col] > new_cost:
                        min_cost[new_row][new_col] = new_cost
                        heapq.heappush(min_heap, (new_cost, new_row, new_col))

        return min_cost[len(grid) - 1][len(grid[0]) - 1]

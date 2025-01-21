from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        first_row_sum = sum(grid[0])
        second_row_sum = 0
        ans = float("inf")

        for i in range(len(grid[0])):
            first_row_sum -= grid[0][i]

            # min() is what first robot wants
            # max() is what second robot wants
            ans = min(ans, max(first_row_sum, second_row_sum))

            # Second is delayed because of first robot move
            second_row_sum += grid[1][i]

        return ans
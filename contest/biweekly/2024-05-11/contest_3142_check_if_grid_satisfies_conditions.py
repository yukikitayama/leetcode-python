"""
Iteration
"""

from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r > 0 and grid[r][c] != grid[r - 1][c]:
                    return False

                if c > 0 and grid[r][c] == grid[r][c - 1]:
                    return False

        return True

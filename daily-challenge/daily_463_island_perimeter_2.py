"""
7 * 4 - 6 * 2 = 28 - 12 - 16
1 * 4 - 0 * 2 = 4
"""

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    ans += 4

                    if r > 0 and grid[r - 1][c] == 1:
                        ans -= 2

                    if c > 0 and grid[r][c - 1] == 1:
                        ans -= 2

        return ans

    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        ans = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    ans += 4

                    for offset_r, offset_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        neighbor_r = r + offset_r
                        neighbor_c = c + offset_c
                        if 0 <= neighbor_r < len(grid) and 0 <= neighbor_c < len(grid[0]):
                            if grid[neighbor_r][neighbor_c] == 1:
                                ans -= 1

        return ans

    def islandPerimeter1(self, grid: List[List[int]]) -> int:
        num_island = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    num_island += 1

        return num_island * 4 - (num_island - 1) * 2

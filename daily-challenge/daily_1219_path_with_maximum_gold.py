"""
DFD with current sum, T: O(N**2M**2)
"""

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def dfs(r, c):

            # Base
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 0

            total_gold = 0

            g = grid[r][c]

            # Mark as visited
            grid[r][c] = 0

            for offset_r, offset_c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                total_gold = max(
                    total_gold,
                    dfs(r + offset_r, c + offset_c)
                )

            # Backtrack
            grid[r][c] = g

            return total_gold + g

        ans = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    ans = max(ans, dfs(r, c))

        return ans

    def getMaximumGold1(self, grid: List[List[int]]) -> int:

        ans = 0

        def dfs(r, c, curr_sum, visited):
            nonlocal ans

            ans = max(ans, curr_sum)

            # print(r, c, curr_sum, visited)

            for offset_r, offset_c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_r = r + offset_r
                next_c = c + offset_c
                if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]):
                    if grid[next_r][next_c] != 0 and (next_r, next_c) not in visited:
                        curr_sum += grid[next_r][next_c]
                        visited.add((next_r, next_c))

                        dfs(next_r, next_c, curr_sum, visited)

                        curr_sum -= grid[next_r][next_c]
                        visited.discard((next_r, next_c))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    curr_sum = grid[r][c]
                    visited = set([(r, c)])
                    dfs(r, c, curr_sum, visited)

        return ans
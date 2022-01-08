"""
- dp
"""


from typing import List
import functools


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        @functools.lru_cache(maxsize=None)
        def dp(row, col1, col2):
            if col1 < 0 or col1 >= n or col2 < 0 or col2 >= n:
                return 0

            ret = 0
            ret += grid[row][col1]

            if col1 != col2:
                ret += grid[row][col2]

            if row != (m - 1):
                ret += max(
                    dp(row + 1, new_col1, new_col2)
                    for new_col1 in [col1 - 1, col1, col1 + 1]
                    for new_col2 in [col2 - 1, col2, col2 + 1]
                )

            return ret

        return dp(0, 0, n - 1)


if __name__ == '__main__':
    grid = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
    print(Solution().cherryPickup(grid))

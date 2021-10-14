"""
1, 4, 5
2, 7 (9 or 7), 6 (6 or 8)
6, 8 (9 or 8), 7 (7 or 9)

- Make cumsum prefix dp array from top left to down right
- when update cell, take minimum of top and left

Example 2
1, 2, 3
4, 5, 6

cumsum prefix array
1, 3, 6
5, 8 (8 or 10), 12 (12 or 14)
"""


from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Base case
        # Row
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        # Column
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]

        # Traverse grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        # Return down right
        return grid[m - 1][n - 1]


grid = [[1,3,1],[1,5,1],[4,2,1]]
print(Solution().minPathSum(grid))



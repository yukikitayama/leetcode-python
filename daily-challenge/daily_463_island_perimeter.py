from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        ans = 0

        for row in range(rows):
            for col in range(cols):

                if row == 0:
                    top = 0
                else:
                    top = grid[row - 1][col]
                if col == 0:
                    left = 0
                else:
                    left = grid[row][col - 1]
                if row == rows - 1:
                    down = 0
                else:
                    down = grid[row + 1][col]
                if col == cols - 1:
                    right = 0
                else:
                    right = grid[row][col + 1]

                if grid[row][col] == 1:
                    ans += 4 - (top + left + down + right)

        return ans


grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
grid = [[1]]
grid = [[1,0]]
print(Solution().islandPerimeter(grid))


from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        for r in range(1, len(grid)):
            grid[r][0] = grid[r - 1][0] + grid[r][0]

        for c in range(1, len(grid[0])):
            grid[0][c] = grid[0][c - 1] + grid[0][c]

        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

        return grid[-1][-1]


if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(Solution().minPathSum(grid))

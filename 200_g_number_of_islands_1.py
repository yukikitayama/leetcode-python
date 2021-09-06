from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case where empty input
        if grid is None or len(grid) == 0:
            return 0

        nr = len(grid)
        nc = len(grid[0])
        num_islands = 0

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_islands += 1
                    self.dfs(grid, r, c)

        return num_islands

    def dfs(self, grid: List[List[str]], r: int, c: int) -> None:
        nr = len(grid)
        nc = len(grid[0])

        # If an element is not a part of the island, return nothing to break outof the recursion
        if r < 0 or c < 0 or r >= nr or c >= nc or grid[r][c] == '0':
            return

        # Make the current element as the sea t avoid visiting here again
        grid[r][c] = '0'

        # Try all the 4 directions by top, down, left, right
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)


"""
Time complexity
Let m the number of rows, n the number of columns. This algorithm goes to all the rows and columns. So O(n*m)
Space complexity
Worst case is all the elements in the grid is filled with a land, and DFS goes to n * m times. So O(n*m)
"""


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid))

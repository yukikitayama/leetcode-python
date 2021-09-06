from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0:
            return 0

        nr = len(grid)
        nc = len(grid[0])
        num_islands = 0

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_islands += 1
                    grid[r][c] = '0'

                    # Assign a unique index to each element in the grid
                    # Starting from 0, ending at r * c - 1, row-wise
                    neighbors = [r * nc + c]

                    while len(neighbors) != 0:
                        id = neighbors.pop(0)
                        # From id to get row and column
                        row = id // nc  # starts from 0, ends at m - 1
                        col = id % nr  # starts from 0, ends at n - 1

                        # Go up, and inside grid, and it's a land
                        if row - 1 >= 0 and grid[row - 1][col] == '1':
                            neighbors.append((row - 1) * nc + col)
                            grid[row - 1][col] = '0'
                        # Go down, and inside grid, and it's a land
                        if row + 1 < nr and grid[row + 1][col] == '1':
                            neighbors.append((row + 1) * nc + col)
                            grid[row + 1][col] = '0'
                        # Go left, and inside grid, and it's a land
                        if col - 1 >= 0 and grid[row][col - 1] == '1':
                            neighbors.append(row * nc + (col - 1))
                            grid[row][col - 1] = '0'
                        # Go right, and inside grid, and it's a land
                        if col + 1 < nc and grid[row][col + 1] == '1':
                            neighbors.append(row * nc + (col + 1))
                            grid[row][col + 1] = '0'

        return num_islands


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
print(Solution().numIslands(grid))

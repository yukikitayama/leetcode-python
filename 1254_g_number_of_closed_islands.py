from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def dfs(i: int, j: int) -> int:

            # Check inside boundary
            # From left to right, once it hits True, meaning out of the boundary,
            # return 0 as not a valid closed island
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0

            # If the current cell in the grid is 1, meaning it's sea, if grid[i][j] is True
            # print(f'before if grid[i][j], i: {i}, j: {j}, grid[i][j]: {grid[i][j]}')
            if grid[i][j]:
                return 1

            # Mark the current cell visited by updating it to 1
            grid[i][j] = 1

            # If all the four directions are islands, the following multiplication can generate
            # 1 * 1 * 1 * 1 and it's 1, so all the four directions needs to be 1 (sea), to get 1 closed island
            # If any of the directions is out of the grid, meaning receiving 0,
            # the result of the multiplication will be 0
            # right * left * down * up
            return dfs(i, j + 1) * dfs(i, j - 1) * dfs(i + 1, j) * dfs(i - 1, j)

        summed = 0

        for i, row in enumerate(grid):

            for j, cell in enumerate(row):

                # When the current cell is island (0), if not 0 is True
                if not cell:
                    summed += dfs(i, j)

        return summed


"""
Time complexity
Let m be the number of rows and n be the number of columns
O(mn) for nested for loops

Space complexity
O(mn) for dfs stack
"""


grid = [
    [1,1,1,1,1,1,1,0],
    [1,0,0,0,0,1,1,0],
    [1,0,1,0,1,1,1,0],
    [1,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0]
]
grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# grid = [
#     [1,1,1,1,1,1,1],
#     [1,0,0,0,0,0,1],
#     [1,0,1,1,1,0,1],
#     [1,0,1,0,1,0,1],
#     [1,0,1,1,1,0,1],
#     [1,0,0,0,0,0,1],
#     [1,1,1,1,1,1,1]
# ]
print(Solution().closedIslands(grid))

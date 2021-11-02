from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        non_obstacles = 0
        start_row = 0
        start_col = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] >= 0:
                    non_obstacles += 1
                if grid[row][col] == 1:
                    start_row = row
                    start_col = col

        def backtracking(row, col, remain):

            nonlocal ans

            if grid[row][col] == 2 and remain == 1:
                ans += 1
                return

            temp = grid[row][col]
            grid[row][col] = -2
            remain -= 1

            for offset_row, offset_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_row = row + offset_row
                next_col = col + offset_col

                if 0 <= next_row < rows and 0 <= next_col < cols:
                    if grid[next_row][next_col] >= 0:
                        backtracking(next_row, next_col, remain)

            # Backtracking
            grid[row][col] = temp

        ans = 0

        backtracking(start_row, start_col, non_obstacles)

        return ans


"""
- Let n be the number of cells in the grid
- At the starting cell it has 4 directions to go, and then it keeps having 3 directions to go,
  because it cannot go back to the previous visited cell, so 4 - 1 = 3. At the ending cell, it
  does not need to try directions any more, so time is O(4 * 3^(n-2)) = O(3^n)
- Space is O(n) because backtracking is recursion, so it has call stack of size n
"""


grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
print(Solution().uniquePathsIII(grid))



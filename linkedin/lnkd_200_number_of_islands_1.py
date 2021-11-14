"""
- Initialize ans to 0
- Iterate each row and column as start cell of DFS
  - If the current cell already visited skip
- DFS
  - No more cell to go, increment ans
"""


from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set([])

        def dfs(row, col):

            # print(f'  visited: {visited}')

            for offset_row, offset_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_row = row + offset_row
                next_col = col + offset_col

                # print(f'    next_row: {next_row}, next_col: {next_col}')

                if (
                        0 <= next_row < len(grid)
                        and 0 <= next_col < len(grid[0])
                        and grid[next_row][next_col] == '1'
                        and (next_row, next_col) not in visited
                ):
                    visited.add((next_row, next_col))
                    dfs(next_row, next_col)

        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                # print(f'row: {row}, col: {col}, {(row, col) not in visited}')

                if grid[row][col] == '1' and (row, col) not in visited:
                    # print(f'  row: {row}, col: {col}')
                    ans += 1
                    visited.add((row, col))
                    dfs(row, col)

        return ans


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



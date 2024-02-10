"""
iterate all cell
  if curr cell is 1
    count up number of island
    dfs

return number of islands

dfs(row, col)
  get next row col
    if next is 1 and in the grid
      in-place modify the grid of the next cell to "0"
      dfs(next row col)

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(row, col):
            for offset_row, offset_col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                next_row = row + offset_row
                next_col = col + offset_col

                if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] == "1":
                    grid[next_row][next_col] = "0"
                    dfs(next_row, next_col)

        ans = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    ans += 1
                    dfs(r, c)

        return ans

from typing import List


class Solution:
    def numIslands_hashset(self, grid: List[List[str]]) -> int:

        visited = set()

        def dfs(row, col):

            visited.add((row, col))

            # up, right, down, left
            for offset_x, offset_y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                next_row = row + offset_x
                next_col = col + offset_y

                if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                    if grid[next_row][next_col] == "1" and (next_row, next_col) not in visited:
                        dfs(next_row, next_col)

        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    ans += 1

        return ans

    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(row, col):
            grid[row][col] = "0"

            # up, right, down, left
            for offset_x, offset_y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                next_row = row + offset_x
                next_col = col + offset_y

                if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                    if grid[next_row][next_col] == "1":
                        dfs(next_row, next_col)

        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1

        return ans
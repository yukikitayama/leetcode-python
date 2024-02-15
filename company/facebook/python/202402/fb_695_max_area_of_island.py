"""
iterate all the cell
  if current cell is 1, bfs
    when vist a cell, in-place modify to 0 to avoid visit again
    every time pop node from queue, count up current area,
    at the end fo bfs return area
  update area if bigger

+ 5 minute
"""

from typing import List
import collections


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # Define bfs
        def bfs(start_row, start_col):
            area = 0
            queue = collections.deque()
            queue.append((start_row, start_col))
            grid[start_row][start_col] = 0

            while queue:

                for _ in range(len(queue)):

                    curr_row, curr_col = queue.popleft()
                    area += 1
                    # print(curr_row, curr_col, area)

                    for offset_row, offset_col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        next_row = curr_row + offset_row
                        next_col = curr_col + offset_col

                        if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] == 1:
                            grid[next_row][next_col] = 0
                            queue.append((next_row, next_col))

            return area

        ans = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    # print(r, c, area)
                    ans = max(ans, area)

        return ans

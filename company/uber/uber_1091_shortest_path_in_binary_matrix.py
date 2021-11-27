"""
- BFS
  - Can append next cell to queue if
    - 0
    - 8 directions
    - in the boundary
  - Queue contains steps
- Return steps
"""


from typing import List
import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return -1

        def get_neighbors(row, col):
            for offset_row, offset_col in [
                (-1, 0), (1, 0), (0, -1), (0, 1),
                (-1, -1), (-1, 1), (1, -1), (1, 1)
            ]:
                next_row = row + offset_row
                next_col = col + offset_col
                if not(0 <= next_row < m and 0 <= next_col < n):
                    continue
                if grid[next_row][next_col] != 0:
                    continue
                yield next_row, next_col

        queue = collections.deque()
        queue.append((0, 0))
        grid[0][0] = 1

        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (m - 1, n - 1):
                return distance

            for next_row, next_col in get_neighbors(row, col):
                grid[next_row][next_col] = distance + 1
                queue.append((next_row, next_col))

        return -1


grid = [[0,0,0],[1,1,0],[1,1,0]]
grid = [[0,1],[1,0]]
print(Solution().shortestPathBinaryMatrix(grid))

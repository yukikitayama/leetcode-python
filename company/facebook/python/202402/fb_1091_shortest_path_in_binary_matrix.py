"""
Algo
  goal false
  BFS
    queue starts from top left
    steps counter starts with 1
    when current queue empty, increment step
    when current cell is bottom right, break goal is true
    append next cell to the queue
      next cell is
        cell is 0
        not visited yet
          visited set
          in-place modify grid from 0 to 1
        8 directional
        in the grid

  return step if goal is true, else -1

Edge
  top left or right bottom is 1
"""

from typing import List
import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        # Edge
        if grid[0][0] == 1 or grid[n - 1][m - 1] == 1:
            return -1

        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        queue = collections.deque()
        queue.append([0, 0])
        grid[0][0] = 1
        goal = False
        steps = 0

        while queue and not goal:

            steps += 1

            for _ in range(len(queue)):

                curr_row, curr_col = queue.popleft()

                if [curr_row, curr_col] == [n - 1, m - 1]:
                    goal = True
                    break

                for offset_row, offset_col in directions:
                    next_row = curr_row + offset_row
                    next_col = curr_col + offset_col

                    if 0 <= next_row < n and 0 <= next_col < m and grid[next_row][next_col] == 0:
                        queue.append([next_row, next_col])
                        grid[next_row][next_col] = 1

        return steps if goal else -1
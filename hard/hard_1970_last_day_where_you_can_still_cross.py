"""
T: O(row col log(row col))
  row col for BFS
  log(row col) for binary search
  for each binary search, it takes BFS
S: O(row col)
  grid space
"""

from typing import List
import collections


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        # BFS
        def can_cross(mid):

            # Initialize grid
            grid = [[0] * col for _ in range(row)]
            # mid is 1-based day and we wanna include it
            # :mid can include becuase array index is 0-based
            for r, c in cells[:mid]:
                # r, c are 1-based index
                grid[r - 1][c - 1] = 1

            # Initialize BFS queue
            queue = collections.deque()
            for c in range(len(grid[0])):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    # Mark as visited
                    grid[0][c] = -1

            while queue:
                for _ in range(len(queue)):
                    curr_r, curr_c = queue.popleft()

                    if curr_r == row - 1:
                        return True

                    for offset_r, offset_c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        next_r = curr_r + offset_r
                        next_c = curr_c + offset_c
                        if 0 <= next_r < row and 0 <= next_c < col and grid[next_r][next_c] == 0:
                            queue.append((next_r, next_c))
                            grid[next_r][next_c] = -1

            return False

        # Binary search
        left = 1
        right = len(cells)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if can_cross(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

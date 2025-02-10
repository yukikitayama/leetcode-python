"""
[2,1,1],
[0,1,1],
[1,0,1]

preprocess
  number of fresh orange
BFS
  count time
  decrement number of fresh orage
if fresh num is 0
  return time
else
  return -1
"""

from typing import List
import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_fresh = 0
        queue = collections.deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    num_fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        # Edge case
        if num_fresh == 0:
            return 0

        # BFS
        # -1 because at the end, t is final time when the last rotten orange is in the queue
        # so when popped, no more rotting happens, but time will be incremented
        t = -1
        while queue:

            for _ in range(len(queue)):

                r, c = queue.popleft()

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    next_r = r + dr
                    next_c = c + dc
                    if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]):
                        if grid[next_r][next_c] == 1:
                            grid[next_r][next_c] = 2
                            num_fresh -= 1
                            queue.append((next_r, next_c))

            t += 1

        return t if num_fresh == 0 else - 1

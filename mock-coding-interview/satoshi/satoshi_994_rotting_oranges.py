"""
[
    [2,1,1],
    [0,1,1],
    [1,0,1]]
Collect all the cells of 2s
BFS
  In-place modify
  answer minutes start with 0,
    max(ans, current minute)
Iterate again
  If I see 1, return -1
Return answer minutes

[
    [2,1,1],
    [1,1,1],
    [0,1,2]
]
exp: 2
out: 3

[
    [2,2],
    [1,1],
    [0,0],
    [2,0]
    ]
exp: 1
out: 2
"""

from typing import List
import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS
        queue = collections.deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))

        minutes = 0

        while queue:

            for _ in range(len(queue)):

                curr_r, curr_c = queue.popleft()

                for offset_r, offset_c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_r = curr_r + offset_r
                    next_c = curr_c + offset_c
                    if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]):
                        if grid[next_r][next_c] == 1:
                            grid[next_r][next_c] = 2
                            queue.append([next_r, next_c])

            minutes += 1

        # Iterate again
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1

        return max(minutes - 1, 0)
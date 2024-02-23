"""
BFS
"""

from typing import List
import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        queue = collections.deque()
        queue.append((0, 0))
        length = 1
        grid[0][0] = 1
        n = len(grid)
        m = len(grid[0])
        offsets = [
            # up, up right, right, down right
            (-1, 0), (-1, 1), (0, 1), (1, 1),
            # down, down left, left, up left
            (1, 0), (1, -1), (0, -1), (-1, -1)
        ]

        while queue:

            for _ in range(len(queue)):

                r, c = queue.popleft()

                print(r, c)

                if r == n - 1 and c == m - 1:
                    return length

                for offset_r, offset_c in offsets:
                    next_r = r + offset_r
                    next_c = c + offset_c

                    if 0 <= next_r < n and 0 <= next_c < m and grid[next_r][next_c] == 0:
                        grid[next_r][next_c] = 1
                        queue.append((next_r, next_c))

            length += 1

        return -1
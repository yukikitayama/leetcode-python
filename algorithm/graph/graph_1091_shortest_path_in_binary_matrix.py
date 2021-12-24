"""
- Spent: 13m
- Solved: 1
- Saw solution: 0
- Optimized: 0
"""


from typing import List
import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # Edge case
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        queue = collections.deque()
        # queue: [(row, col, distance), ...]
        queue.append((0, 0, 1))

        offset = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (-1, 1), (1, 1), (1, -1), (-1, -1)
        ]

        while queue:

            for _ in range(len(queue)):

                curr_row, curr_col, distance = queue.popleft()

                if curr_row == (len(grid) - 1) and curr_col == (len(grid[0]) - 1):
                    return distance

                for offset_row, offset_col in offset:

                    next_row = curr_row + offset_row
                    next_col = curr_col + offset_col

                    if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                        if grid[next_row][next_col] == 0:
                            queue.append((next_row, next_col, distance + 1))
                            grid[next_row][next_col] = 1

        return -1


grid = [[0,1],[1,0]]
# 2
grid = [[0,0,0],[1,1,0],[1,1,0]]
# 4
# grid = [
#     [1, 0, 0],
#     [1, 1, 0],
#     [1, 1, 0]
# ]
# -1 because the first top-left cell is 1, not 0.
print(Solution().shortestPathBinaryMatrix(grid))

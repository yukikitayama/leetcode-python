"""
[
[1,0,1],
[1,0,0],
[1,0,0]
]

row
Counter({0: 2, 1: 1, 2: 1})
col
Counter({0: 3, 2: 1})

(0, 0): (2 - 1) * (3 - 1) = 1 * 2 = 2
(0, 2): (2 - 1) * (1 - 1) = 1 * 0 = 0
(1, 0): 0 * 2 = 0
"""

from typing import List
import collections


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        row_counter = collections.Counter()
        col_counter = collections.Counter()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    row_counter[r] += 1
                    col_counter[c] += 1

        # print(row_counter)
        # print(col_counter)

        ans = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    ans += (row_counter[r] - 1) * (col_counter[c] - 1)

        return ans
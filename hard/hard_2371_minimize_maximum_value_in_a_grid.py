from typing import List


class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        vals = []
        for r in range(m):
            for c in range(n):
                vals.append((grid[r][c], r, c))
        vals.sort()

        # print(vals)

        row_max = [0] * m
        col_max = [0] * n

        for _, r, c in vals:

            # Start with 1 because we need to replace a value with a positive integer, no 0
            curr_val = max(row_max[r], col_max[c]) + 1

            row_max[r] = curr_val
            col_max[c] = curr_val

            grid[r][c] = curr_val

            # print(_, r, c)
            # for row in grid:
            #     print(row)
            # print(row_max)
            # print(col_max)
            # print()

        return grid

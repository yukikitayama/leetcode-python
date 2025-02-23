from typing import List
import functools


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:

        # Clockwise: bottom right, bottom left, top left, top right
        ds = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
        n = len(grid)
        m = len(grid[0])
        # If current is 1, then next is 2
        # If current is 2, then next is 0
        # If current is 0, then next is 2
        nx = [2, 2, 0]

        @functools.cache
        def dp(i, j, x, d, k):
            """
            i: row, j: col
            x: cell value we are looking for
            d: direction
            k: Remaining turn, 1 or 0
            """

            # Base: Out of grid
            if not (0 <= i < n and 0 <= j < m):
                return 0

            # Base: current cell doesn't have the value we are looking for
            if grid[i][j] != x:
                return 0

            # Transition
            next_i = i + ds[d][0]
            next_j = j + ds[d][1]
            next_x = nx[x]
            # Option 1: Keep the same direction, and no turn
            res = dp(next_i, next_j, next_x, d, k) + 1

            # Option 2: Turn 90 degree to right, if haven't turned yet
            if k > 0:
                next_d = (d + 1) % 4
                next_i = i + ds[next_d][0]
                next_j = j + ds[next_d][1]
                next_x = nx[x]
                # 0 because no more turn left
                res2 = dp(next_i, next_j, next_x, next_d, 0) + 1
                res = max(res, res2)

            return res

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cur = max(dp(i, j, 1, d, 1) for d in range(4))
                    ans = max(cur, ans)

        return ans
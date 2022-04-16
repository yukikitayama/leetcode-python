"""
- Skyline from top
  - [max(col_0), max(col_1), ...]
- Skyline from  left
  - [max(row_0), max(row_1), ...]
"""


from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # From left and right
        row_maxes = [max(row) for row in grid]
        # *grid unpacks each row, zip() allows us to iterate the elements in each row at the same time
        # so meaning iterating column
        # From top and bottom
        col_maxes = [max(col) for col in zip(*grid)]

        ans = 0

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                ans += (min(row_maxes[r], col_maxes[c]) - val)

        return ans


if __name__ == '__main__':
    grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    # 35
    print(Solution().maxIncreaseKeepingSkyline(grid))

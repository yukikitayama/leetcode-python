"""
- Binary search in each row to have T: O(MlogN) M: row, N: column
- Staircase to have T: O(M + N)
"""


from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        r = m - 1
        c = 0
        ans = 0

        while r >= 0 and c < n:

            if grid[r][c] < 0:
                ans += n - c
                r -= 1

            else:
                c += 1

        return ans


if __name__ == '__main__':
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    # 8
    print(Solution().countNegatives(grid))

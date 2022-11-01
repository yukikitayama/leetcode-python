"""
- Ball can move if current cell has the same value as the adjacent column
"""


from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

        def find_column(row, col):

            # Reaching bottom, which means we need to return the column index because fallout
            if row == len(grid):
                return col

            # grid[row][col] is 1 if right, -1 if left
            # so by addition, we can get next column index
            next_column = col + grid[row][col]

            if next_column < 0 or next_column >= len(grid[0]) or grid[row][col] != grid[row][next_column]:
                return -1

            return find_column(row + 1, next_column)

        ans = [None for _ in range(len(grid[0]))]

        for i in range(len(grid[0])):
            ans[i] = find_column(0, i)

        return ans


if __name__ == '__main__':
    grid = [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]
    print(Solution().findBall(grid))

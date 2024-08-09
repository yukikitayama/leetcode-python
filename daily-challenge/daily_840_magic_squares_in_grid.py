from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def is_magic_square(row, col):

            # seen[0] won't be used
            seen = [False] * 10

            # Check number range and distinct
            for r in range(3):
                for c in range(3):
                    num = grid[row + r][col + c]
                    # Number range
                    if num < 1 or num > 9:
                        return False
                    # Distinct
                    if seen[num]:
                        return False

                    seen[num] = True

            # Check diagonal sum equality
            diagonal_top_left = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
            diagonal_top_right = grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]
            if diagonal_top_left != diagonal_top_right:
                return False

            # Row sum
            row1 = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]
            row2 = grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2]
            row3 = grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]
            if row1 != diagonal_top_left or row2 != diagonal_top_left or row3 != diagonal_top_left:
                return False

            # Col sum
            col1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
            col2 = grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]
            col3 = grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]
            if col1 != diagonal_top_left or col2 != diagonal_top_left or col3 != diagonal_top_left:
                return False

            return True

        ans = 0

        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):

                if is_magic_square(row, col):
                    ans += 1

        return ans

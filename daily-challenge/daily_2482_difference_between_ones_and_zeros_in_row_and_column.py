"""
2 passes, 1 pass to count, 1 pass to make diff matrix
"""


from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ones_row = [0] * len(grid)
        ones_col = [0] * len(grid[0])
        zeros_row = [0] * len(grid)
        zeros_col = [0] * len(grid[0])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    ones_row[r] += 1
                    ones_col[c] += 1
                else:
                    zeros_row[r] += 1
                    zeros_col[c] += 1

        ans = [[0] * len(grid[0]) for _ in range(len(grid))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ans[r][c] = ones_row[r] + ones_col[c] - zeros_row[r] - zeros_col[c]

        return ans


if __name__ == "__main__":
    grid = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]
    grid = [[1, 1, 1], [1, 1, 1]]
    print(Solution().onesMinusZeros(grid))

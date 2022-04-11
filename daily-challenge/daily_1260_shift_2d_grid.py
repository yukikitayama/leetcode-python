from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        ans = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                row_count, n_c = divmod(c + k, n)
                n_r = (r + row_count) % m
                ans[n_r][n_c] = grid[r][c]

        return ans


if __name__ == '__main__':
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    # [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
    grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
    k = 4
    # [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]+
    print(Solution().shiftGrid(grid, k))

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        # for row in grid:
        #     print(row)

        ans = 0
        c = len(grid[0]) - 1

        for r in range(len(grid)):

            while c >= 0 and grid[r][c] < 0:
                c -= 1

            ans += len(grid[0]) - c - 1

        return ans

    def countNegatives1(self, grid: List[List[int]]) -> int:

        def binary_search(row):
            left = 0
            right = len(row) - 1

            while left <= right:

                mid = (left + right) // 2

                if row[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        ans = 0

        for row in grid:
            res = binary_search(row)
            # print(res)
            ans += (len(row) - res)

        return ans

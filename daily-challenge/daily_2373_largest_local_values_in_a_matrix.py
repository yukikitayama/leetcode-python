from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        def find_max(r, c):
            ans = float("-inf")
            for offset_r in [-1, 0, 1]:
                for offset_c in [-1, 0, 1]:
                    ans = max(
                        ans,
                        grid[r + offset_r][c + offset_c]
                    )
            return ans

        ans = [[None] * (len(grid) - 2) for _ in range(len(grid) - 2)]

        for r in range(len(grid) - 2):
            center_r = r + 1
            for c in range(len(grid) - 2):
                center_c = c + 1
                ans[r][c] = find_max(center_r, center_c)

        return ans

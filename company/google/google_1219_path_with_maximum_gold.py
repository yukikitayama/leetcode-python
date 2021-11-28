from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # (0, 1), (1, 0), (0, -1), (-1, 0)
        DIR = [0, 1, 0, -1, 0]

        def dfs(r, c):

            # If out of bound, or the current cell does not have gold, meaning you cannot visit there
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] == 0:
                return 0

            # For max to work, we need to initialize ans as 0
            # At the deepest, the cell has gold but neighbors do not,
            # In that case, ans is 0 but grid[r][c] is some gold, so
            # return ans + grid[r][c] can correctly return the gold only at the cell
            # And it will recursively accumulated in for loop with max iteration
            # So it's okay to start with ans = 0
            ans = 0

            # To avoid visiting the same cell, mark it as 0,
            # but it will recover the amount with original_gold for the next iteration
            # To be able to put back in, save the gold to temporary original_gold
            original_gold = grid[r][c]
            grid[r][c] = 0

            for i in range(4):
                ans = max(ans, dfs(r + DIR[i], c + DIR[i + 1]))

            grid[r][c] = original_gold
            return ans + grid[r][c]

        ans = 0

        for r in range(m):

            for c in range(n):

                ans = max(ans, dfs(r, c))

        return ans


"""
Time complexity
- The first cell has 4 neighbors to go, and the constraint says at most 25 cell (k) having gold, 
  so starting cells are 25, so 4 * k
- (k - 3) cells have up to 3 neighbors, because it cannot go back to the previous cell, 4 - 1 = 3, and
  3 is 1. start cell (4 ways to go), 2. the second from the last (1 way to go), and 3. the last (No way to go)
So, O(k * 4 * 3^(k - 3)) = O(k3^k)

Space complexity  
O(k) for DFS stack
"""


grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
# grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
print(Solution().getMaximumGold(grid))

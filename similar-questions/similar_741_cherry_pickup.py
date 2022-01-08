"""
- similar to 1463 Cherry Pickup II
"""


from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        memo = [[[None] * n for _ in range(n)] for _ in range(n)]

        def dp(row1, col1, col2):
            row2 = row1 + col1 - col2

            if (
                row1 == n or row2 == n or col1 == n or col2 == n
                or grid[row1][col1] == -1 or grid[row2][col2] == -1
            ):
                return float('-inf')

            # Person 1 reaches bottom-right corner
            elif row1 == col1 == n - 1:
                return grid[row1][col1]

            elif memo[row1][col1][col2]:
                return memo[row1][col1][col2]

            else:
                ans = grid[row1][col1] + grid[row2][col2] * (col1 != col2)
                ans += max(
                    # Person 1 and 2 go right
                    dp(row1, col1 + 1, col2 + 1),
                    # Person 1 go down, person 2 go right
                    dp(row1 + 1, col1, col2 + 1),
                    # Person 1 go right, person 2 go down
                    dp(row1, col1 + 1, col2),
                    # Person 1 and 2 go down
                    dp(row1 + 1, col1, col2)
                )

            memo[row1][col1][col2] = ans

            return ans

        return max(0, dp(0, 0, 0))


if __name__ == '__main__':
    grid = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
    # 5
    grid = [
        [1, 1, -1],
        [1, -1, 1],
        [-1, 1, 1]
    ]
    # 0
    print(Solution().cherryPickup(grid))

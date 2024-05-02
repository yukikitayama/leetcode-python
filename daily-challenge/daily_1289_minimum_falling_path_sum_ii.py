from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dp = [[float("inf")] * n for _ in range(n)]

        # Base case
        first_min_c = None
        second_min_c = None
        for c in range(n):
            dp[n - 1][c] = grid[n - 1][c]

            if first_min_c is None or dp[n - 1][c] <= dp[n - 1][first_min_c]:
                second_min_c = first_min_c
                first_min_c = c
            elif second_min_c is None or dp[n - 1][c] <= dp[n - 1][second_min_c]:
                second_min_c = c

        # State transition
        for r in range(n - 2, -1, -1):

            curr_first_min_c = None
            curr_second_min_c = None

            for c in range(n):
                if c != first_min_c:
                    dp[r][c] = grid[r][c] + dp[r + 1][first_min_c]
                else:
                    dp[r][c] = grid[r][c] + dp[r + 1][second_min_c]

                if curr_first_min_c is None or dp[r][c] <= dp[r][curr_first_min_c]:
                    curr_second_min_c = curr_first_min_c
                    curr_first_min_c = c
                elif curr_second_min_c is None or dp[r][c] <= dp[r][curr_second_min_c]:
                    curr_second_min_c = c

            first_min_c = curr_first_min_c
            second_min_c = curr_second_min_c

        return dp[0][first_min_c]

    def minFallingPathSum3(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dp = [[float("inf")] * n for _ in range(n)]

        # Base case
        for c in range(n):
            dp[n - 1][c] = grid[n - 1][c]

        # State transition
        # n - 2 because n - 1 was already filled
        for r in range(n - 2, -1, -1):
            for c in range(n):
                prev_min = float("inf")
                for prev_c in range(n):
                    if prev_c != c:
                        prev_min = min(prev_min, dp[r + 1][prev_c])

                dp[r][c] = grid[r][c] + prev_min

        ans = float("inf")
        for c in range(n):
            ans = min(ans, dp[0][c])

        return ans

    def minFallingPathSum2(self, grid: List[List[int]]) -> int:
        n = len(grid)

        memo = {}

        def recursion(r, c):

            # Terminate
            if r == n - 1:
                return grid[r][c]

            if (r, c) in memo:
                return memo[(r, c)]

            next_min = float("inf")
            for next_c in range(n):
                if next_c != c:
                    next_min = min(next_min, recursion(r + 1, next_c))

            memo[(r, c)] = grid[r][c] + next_min

            return memo[(r, c)]

        ans = float("inf")

        for c in range(n):
            ans = min(ans, recursion(0, c))

        return ans

    def minFallingPathSum1(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid) for _ in range(len(grid))]

        # Base
        for i in range(len(grid)):
            dp[0][i] = grid[0][i]

        # State transition
        for r in range(1, len(grid)):
            for c in range(len(grid)):
                if c == 0:
                    dp[r][c] = grid[r][c] + dp[r - 1][c + 1]

                elif c == len(grid) - 1:
                    dp[r][c] = grid[r][c] + dp[r - 1][c - 1]

                else:
                    dp[r][c] = grid[r][c] + min(
                        dp[r - 1][c - 1],
                        dp[r - 1][c + 1]
                    )

        for row in grid:
            print(row)
        print()
        for row in dp:
            print(row)

        return min(dp[-1])
"""
min, current depends on previous
Dynamic programming + greedy

i: 0, [3,5,7],color: 1
i: 1, [6,2,9],color: 2
i: 2, [4,8,1],cannot choose 2 (prev) and 2 (equi d -> i = n - i -> 2 = 3 - 2 = 1)
i: 3, [7,3,5] e_d -> i = n - i -> 3 = 3 - 3 = 0

eg2
[2,4,6], sum    color
[5,3,8], [9, 5, 10] [2, 1, 1] color: 3
[7,1,9], [12, 10, 14] [2, ] 2
[4,6,2], color: 2
[3,5,7], 1, min(1, 3)
[8,2,4]
"""

from typing import List

class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        dp = [[float("inf")] * 3 for _ in range(n)]
        # Base
        dp[0] = cost[0]
        colors = []

        for r in range(1, n):
            for c in range(3):
                # n: 6, H1: 0, 1, 2, H2: 3, 4, 5
                if r < (r / n):
                    if c == 0:
                        dp[r][c] = min(dp[r - 1][1], dp[r - 1][2]) + cost[r][c]
                    elif c == 1:
                        dp[r][c] = min(dp[r - 1][0], dp[r - 1][2]) + cost[r][c]
                    elif c == 2:
                        dp[r][c] = min(dp[r - 1][0], dp[r - 1][1]) + cost[r][c]
                    # Saved color
                else:
                    equidistant_index = n - r
                    if c == 0:
                        equidistant_color = colors[equidistant_index]
                        # cannot choose
                        # pick one

        for row in dp:
            print(row)

        print(min(dp[-1]))

        return min(dp[-1])

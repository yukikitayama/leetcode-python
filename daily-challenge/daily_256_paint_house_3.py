"""
1r
  2g
    3r
    3b
  2b
    3r
    3g
1g
  2r
    3g
    3b
  2b
    3r
    3g
1b
  2r
    3g
    3b
  2g
    3r
    3b

dp(i, j)
  argument
    i: index to costs
    j: color index
  base case
    i < 0, cost is 0
  recurrence
    if j == 0, cost = min(costs[i][0] + costs[i - 1][1], costs[i][0] + costs[i - 1][2]
  return
    mininum cost up to ith index cost with j color

solution is min(
  dp(len(costs) - 1, 0),
  dp(len(costs) - 1, 1),
  dp(len(costs) - 1, 2)
)
"""

from typing import List
import functools


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(i, j):

            # Base case
            if i < 0:
                return 0

            if j == 0:
                return costs[i][0] + min(dp(i - 1, 1), dp(i - 1, 2))
            elif j == 1:
                return costs[i][1] + min(dp(i - 1, 0), dp(i - 1, 2))
            elif j == 2:
                return costs[i][2] + min(dp(i - 1, 0), dp(i - 1, 1))

        ans = float("inf")

        for color in range(3):
            ans = min(ans, dp(len(costs) - 1, color))

        return ans


if __name__ == "__main__":
    costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
    # 10
    # costs = [[7, 6, 2]]
    # 2
    print(Solution().minCost(costs))







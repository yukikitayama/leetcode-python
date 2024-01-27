""""
dp(i)
  function
    base case, if i < 0, cost is 0
    nums[i] + dp(i - 1)
    or nums[i] + df(i - 2)
  argument
    index to cost array
  return
    minimum cost up to i
    so our answer is dp(len(cost) - 1)
"""



from typing import List
import functools


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(i):

            # Base case
            if i < 0:
                return 0

            if i == len(cost):
                return min(dp(i - 1), dp(i - 2))
            else:
                return min(
                    cost[i] + dp(i - 1),
                    cost[i] + dp(i - 2)
                )

        return dp(len(cost))


if __name__ == "__main__":
    cost = [10, 15, 20]  # 15
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]  # 6
    print(Solution().minCostClimbingStairs(cost))

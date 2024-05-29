from typing import List
import functools


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        # Preprocess to make top-down DP easier
        cuts = [0] + sorted(cuts) + [n]

        # print(cuts)

        @functools.cache
        def dp(left, right):

            # Base case: Current fragment doesn't contain cutting position
            if left + 1 == right:
                return 0

            ans = float("inf")

            for mid in range(left + 1, right):
                ans = min(
                    ans,
                    # cuts[right] - cuts[left]: Cost equal to length
                    dp(left, mid) + dp(mid, right) + cuts[right] - cuts[left]
                )

            return ans

        return dp(0, len(cuts) - 1)
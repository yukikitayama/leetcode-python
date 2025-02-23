"""
centroid
when k = 1, should be median
  e.g., [4, 8, 20], median: 8, if increment or decrement, total distance will increase, becuase only one house gain and the other 2 houses lose.
when k = n, put a mailbox at every house.

DP is a careful brute force
"""

from typing import List
import functools


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:

        houses.sort()

        @functools.cache
        def dp(left, right, num):

            # More mailboxes than houses: Failed case, we should ignore, so return a huge number
            if right - left + 1 < num:
                return float("inf")

            # Base: only one mailbox left
            if num == 1:
                mid = (left + right) // 2
                # Compute distance
                res = 0
                for i in range(left, right + 1):
                    res += abs(houses[i] - houses[mid])
                return res

            # Base: Each house has one mailbox
            if num == right - left + 1:
                return 0

            res = float("inf")
            # Careful brute force
            for i in range(left, right):
                # Cur current range into two
                res = min(
                    res,
                    dp(left, i, 1) + dp(i + 1, right, num - 1)
                )

            return res

        return dp(0, len(houses) - 1, k)

    def minDistance1(self, houses: List[int], k: int) -> int:

        houses.sort()

        # +1 to k because, e.g., when k = 1, we need to have one case for k = 0 and one case for k = 1
        memo = [[[-1] * len(houses) for _ in range(len(houses))] for _ in range(k + 1)]

        def dp(left, right, num):

            # Cache hit
            if memo[num][left][right] != -1:
                return memo[num][left][right]

            # More mailboxes than houses: Failed case, we should ignore, so return a huge number
            if right - left + 1 < num:
                return float("inf")

            # Base: only one mailbox left
            if num == 1:
                mid = (left + right) // 2
                # Compute distance
                res = 0
                for i in range(left, right + 1):
                    res += abs(houses[i] - houses[mid])
                memo[num][left][right] = res
                return memo[num][left][right]

            # Base: Each house has one mailbox
            if num == right - left + 1:
                return 0

            res = float("inf")
            # Careful brute force
            for i in range(left, right):
                # Cur current range into two
                res = min(
                    res,
                    dp(left, i, 1) + dp(i + 1, right, num - 1)
                )

            memo[num][left][right] = res
            return res

        return dp(0, len(houses) - 1, k)
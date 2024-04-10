"""
Sort pairs by left
Dp
"""

from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        curr_end = float("-inf")
        ans = 0

        for i in range(len(pairs)):

            if curr_end < pairs[i][0]:
                curr_end = pairs[i][1]
                ans += 1

        return ans

    def findLongestChain1(self, pairs: List[List[int]]) -> int:
        pairs.sort()

        dp = [1] * len(pairs)

        ans = 1

        for right in range(1, len(pairs)):
            for left in range(right):
                if pairs[left][1] < pairs[right][0]:
                    dp[right] = max(dp[right], 1 + dp[left])
            ans = max(ans, dp[right])

        return ans

    def findLongestChain1(self, pairs: List[List[int]]) -> int:
        pairs.sort()

        dp = [1] * len(pairs)

        ans = 1

        for left in range(len(pairs) - 1, -1, -1):
            for right in range(left + 1, len(pairs)):
                if pairs[left][1] < pairs[right][0]:
                    dp[left] = max(dp[left], 1 + dp[right])
            ans = max(ans, dp[left])

        return ans
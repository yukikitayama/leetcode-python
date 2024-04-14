"""
% difference?
"""

from typing import List
import collections


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        num_to_length = collections.defaultdict(int)
        ans = 1

        for i in range(len(arr)):

            if arr[i] - difference in num_to_length:
                num_to_length[arr[i]] = 1 + num_to_length[arr[i] - difference]

            else:
                num_to_length[arr[i]] = 1

            ans = max(ans, num_to_length[arr[i]])

        return ans

    def longestSubsequence1(self, arr: List[int], difference: int) -> int:
        dp = [1] * len(arr)

        for right in range(1, len(arr)):
            for left in range(right):
                if arr[right] - arr[left] == difference:
                    dp[right] = max(dp[right], 1 + dp[left])

        return max(dp)
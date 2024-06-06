from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        # Base case: keep each column
        # Represents the number of columns to keep
        dp = [1] * len(strs[0])

        for left in range(len(strs[0]) - 2, -1, -1):
            for right in range(left + 1, len(strs[0])):
                if all(str_[left] <= str_[right] for str_ in strs):
                    dp[left] = max(dp[left], 1 + dp[right])

        return len(strs[0]) - max(dp)

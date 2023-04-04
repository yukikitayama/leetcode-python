"""
Sliding window
"""


class Solution:
    def partitionString(self, s: str) -> int:

        last_seen = [-1] * 26
        ans = 1
        start = 0

        for i in range(len(s)):

            if last_seen[ord(s[i]) - ord("a")] >= start:

                ans += 1
                start = i

            last_seen[ord(s[i]) - ord("a")] = i

        return ans

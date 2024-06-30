"""
Hashset and sliding window
"""


class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        chars = set()
        left = 0
        ans = 0

        for right in range(len(s)):

            while s[right] in chars:
                chars.discard(s[left])
                left += 1

            chars.add(s[right])

            ans += len(chars)

        return ans
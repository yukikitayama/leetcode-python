"""
palindrome
all even
or one odd and other even

collect all even, then if odd exists, then plus 1

e.g.
ccc
"""

import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_exist = False
        counter = collections.Counter(s)
        ans = 0

        for k, v in counter.items():
            if v % 2 == 0:
                ans += v
            else:
                odd_exist = True
                ans += v - 1

        return ans + 1 if odd_exist else ans

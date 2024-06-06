"""
The base cases of this recursive function are the substrings entirely consisting of the same character. For such of these substrings, solve(l,r)=0\text{solve}(l, r) = 0solve(l,r)=0, since one does not have to do any operations.
"""

import functools


class Solution:
    def strangePrinter(self, s: str) -> int:

        @functools.cache
        def dp(l, r):

            res = len(s)

            # Variable to used to identify if substring is one characters or all the characters
            # are the same
            sub_l = -1

            for sub_r in range(l, r):

                if s[sub_r] != s[r] and sub_l == -1:
                    sub_l = sub_r

                if sub_l != -1:
                    res = min(
                        res,
                        1 + dp(sub_l, sub_r) + dp(sub_r + 1, r)
                    )

            # Current substring contains only one character,
            # or all the characters are the same
            # so no operation is needed
            if sub_l == -1:
                # print(l, r, sub_l, s[l:r])
                res = 0

            return res

        # +1 because, even if s is all the same characters,
        # we need to perform one operations to print those same characters
        return dp(0, len(s) - 1) + 1
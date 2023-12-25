"""
sliding window
"""

import functools


class Solution:
    def numDecodings(self, s: str) -> int:

        @functools.cache
        def recursion(index, s):

            if index == len(s):
                return 1

            if s[index] == "0":
                return 0

            if index == len(s) - 1:
                return 1

            ans = recursion(index + 1, s)

            if int(s[index:index + 2]) <= 26:
                ans += recursion(index + 2, s)

            return ans

        return recursion(0, s)


if __name__ == "__main__":
    s = "326"
    s = "06"
    s = "10"
    print(Solution().numDecodings(s))

"""
subproblem affect other problems
think as finding minimum number of removing charaters as it sounds like dp
and return t or f if the minimum number is <= k
dp
try top-down dp

every index keep or remove, and remaining k
"""

import functools


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        @functools.lru_cache(maxsize=None)
        def dp(left, right):

            # Base case, 1 character left
            if left == right:
                return 0

            # Base case, 2 characters left
            if left == right - 1:
                if s[left] != s[right]:
                    return 1
                else:
                    return 0

            # If same characters, no need to remove
            if s[left] == s[right]:
                return dp(left + 1, right - 1)

            # If different character, need to remove so 1, and decide whether remove left or right
            # but take minimum number
            else:
                return 1 + min(dp(left + 1, right), dp(left, right - 1))

        return dp(0, len(s) - 1) <= k


if __name__ == "__main__":
    s = "abcdeca"
    k = 2
    # T

    s = "abbababa"
    k = 1
    # T

    print(Solution().isValidPalindrome(s, k))

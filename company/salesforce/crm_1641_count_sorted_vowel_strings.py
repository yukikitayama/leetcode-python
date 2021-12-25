"""
- dp?
- backtracking?
"""


import functools


# Top-down DP
class Solution:
    def countVowelStrings(self, n: int) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(n, vowels):
            if n == 1:
                return vowels

            if vowels == 1:
                return 1

            ans = dp(n - 1, vowels) + dp(n, vowels - 1)

            return ans

        return dp(n, 5)


# Backtracking
class Solution1:
    def countVowelStrings(self, n: int) -> int:

        def recursion(n, vowels):
            # Reach the end
            if n == 0:
                return 1

            ans = 0
            # 5 is the number of vowels; a, e, i, o, u
            for i in range(vowels, 5 + 1):
                ans += recursion(n - 1, i)

            return ans

        return recursion(n, 1)


if __name__ == '__main__':

    n = 1
    # 5
    n = 2
    # 15
    n = 33
    # 66045
    print(Solution().countVowelStrings(n))



"""
binary keep/remove choice for each s1 character
and binary keep/remove choice for each s2 character

if keep, dp(i + 1)
if remove, dp(i + 1) + ascii
  if remove, we have 3 choices,
    remove one character from s1
    remove one character from s2
    remove one character from both s1 and s2

min(keep, remove)

Base case, when strings are empty
  if s1 is empty, remove all s2
  if s2 is empty, remove all s1
  if both s1 and s2 are empty, no deletion
"""

import functools


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(i, j):

            # Base case, deletion is not needed
            if i < 0 and j < 0:
                return 0

            if i < 0:
                return ord(s2[j]) + dp(i, j - 1)

            if j < 0:
                return ord(s1[i]) + dp(i - 1, j)

            # If characters are equal, no deletion is needed, move to next character
            if s1[i] == s2[j]:
                return dp(i - 1, j - 1)
            else:
                return min(
                    ord(s1[i]) + dp(i - 1, j),
                    ord(s2[j]) + dp(i, j - 1)
                )

        return dp(len(s1) - 1, len(s2) - 1)







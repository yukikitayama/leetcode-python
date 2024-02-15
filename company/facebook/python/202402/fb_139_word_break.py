"""
two pointers
  left as substring beginning
    fix left
  right as substring ending
    iterate right from left to end
  if substring exists in dictionary
    right + 1 will be the next left

Memoization
  k: (left, right)
  v: T/F
"""

from typing import List
import functools


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @functools.lru_cache(maxsize=None)
        def dp(right):

            # Terminal
            if right < 0:
                return True

            for word in wordDict:
                # s: aabcd, word: abc, right: 3
                if s[right - len(word) + 1:right + 1] == word and dp(right - len(word)):
                    return True

            return False

        return dp(len(s) - 1)

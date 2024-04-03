from typing import List
import functools


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)

        for i in range(len(s)):
            for word in wordDict:

                # Skip impossible case
                # len: 2, len - 1: 1, ending at 0 cannot create length 2 word
                # but i: 1, ending at 1 can create length 2 word by at 0 and at 1
                if i < len(word) - 1:
                    continue

                # First word, or build on top of the previous word
                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1:i + 1] == word:
                        dp[i] = True
                        break

        return dp[-1]

    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:

        @functools.lru_cache(maxsize=None)
        def dp(i):

            # Base: No characters to process
            if i < 0:
                return True

            ans = False
            for word in wordDict:
                # s: abcd, word: bcd, i: 3, len: 3
                start = i - len(word) + 1
                # i is current end index
                if s[start:i + 1] == word and dp(i - len(word)):
                    ans = True

            return ans

        return dp(len(s) - 1)
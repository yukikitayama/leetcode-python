"""
Bottom-up dynamic programming
dp[i] represents substring starting from beginning to index i satisfies the requirement
that s[beginnig to i] can be segmented into a space-separated sequence of
one or more dictionary words
"""


from typing import List
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        # + 1 for empty word
        dp = [False] * (len(s) + 1)

        # Base case
        dp[0] = True

        # i is ending index of substring from s
        for i in range(1, len(s) + 1):

            # print(f'i: {i}')

            for j in range(i):

                # print(f'  j: {j}, dp[j]: {dp[j]}, s[j:i]: {s[j:i]}')

                # Need dp[j] otherwise words will overlap in s
                if dp[j] and s[j:i] in word_set:
                # if s[j:i] in word_set:

                    # print(f'    dp[j]: {dp[j]}, s[j:i]: {s[j:i]}')

                    dp[i] = True

        # print(f'dp: {dp}')

        return dp[len(s)]


# s = "leetcode"
# wordDict = ["leet","code"]
# s = "applepenapple"
# wordDict = ["apple","pen"]
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
# Expected: false
print(Solution().wordBreak(s, wordDict))


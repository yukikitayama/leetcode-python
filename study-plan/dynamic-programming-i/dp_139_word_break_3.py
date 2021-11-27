"""
Recursion with memoization
"""


from typing import List
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @lru_cache(maxsize=None)
        def wordBreakMemo(s, word_dict, start):
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):

                curr_word = s[start:end]

                if curr_word in word_dict and wordBreakMemo(s, word_dict, end):
                    return True

            return False

        return wordBreakMemo(s, tuple(wordDict), 0)


s = "leetcode"
wordDict = ["leet","code"]
# s = "applepenapple"
# wordDict = ["apple","pen"]
# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
print(Solution().wordBreak(s, wordDict))


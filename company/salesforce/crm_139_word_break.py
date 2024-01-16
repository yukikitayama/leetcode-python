"""
recursion
hashset
"""

from typing import List
import collections
import functools


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        words = set(wordDict)
        queue = collections.deque([0])
        seen = set()

        while queue:

            start = queue.popleft()

            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):

                if end in seen:
                    continue

                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)

        return False


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @functools.lru_cache(maxsize=None)
        def recursion(i):
            if i < 0:
                return True

            for word in wordDict:
                # len(word) + 1 because of 0-index to be inclusive
                # i + 1 to be exclusive
                if s[i - len(word) + 1:i + 1] == word and recursion(i - len(word)):
                    return True

            return False

        return recursion(len(s) - 1)


if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]

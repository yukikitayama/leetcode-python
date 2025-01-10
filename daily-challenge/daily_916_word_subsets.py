"""
brute force
  counter
"""

from typing import List
import collections


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_chars = [0] * 26
        for word2 in words2:
            counter = collections.Counter(word2)
            for k, v in counter.items():
                i = ord(k) - ord("a")
                max_chars[i] = max(
                    max_chars[i],
                    v
                )

        # print(max_chars)

        ans = []

        for word1 in words1:

            counter = collections.Counter(word1)
            universal = True
            for i in range(len(max_chars)):
                k = chr(ord("a") + i)
                if counter[k] < max_chars[i]:
                    universal = False
            if universal:
                ans.append(word1)

        return ans


    def wordSubsets1(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []

        for word1 in words1:
            c1 = collections.Counter(word1)
            universal = True
            for word2 in words2:
                c2 = collections.Counter(word2)
                if not c2 <= c1:
                    universal = False
            if universal:
                ans.append(word1)

        return ans
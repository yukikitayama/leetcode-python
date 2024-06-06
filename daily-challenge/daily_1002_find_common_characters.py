from typing import List
import collections


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = collections.Counter(words[0])

        for word in words[1:]:

            counter &= collections.Counter(word)

        ans = []

        for k, v in counter.items():

            for _ in range(v):

                ans.append(k)

        return ans
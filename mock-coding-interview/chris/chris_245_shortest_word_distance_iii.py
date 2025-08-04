from typing import List


class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ans = float("inf")

        prev = -1
        for i in range(len(wordsDict)):

            if wordsDict[i] == word1 or wordsDict[i] == word2:

                if prev != -1 and (wordsDict[prev] != wordsDict[i] or word1 == word2):

                    ans = min(ans, i - prev)

                prev = i

        return ans
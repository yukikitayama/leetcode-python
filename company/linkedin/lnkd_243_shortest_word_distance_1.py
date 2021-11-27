"""
- make hashmap with key word and value a list of indices
- with given two words, get the two lists, and find the min abs difference between two indices

- Keep the most recent indices of word1 and word2
"""


from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        idx_1 = idx_2 = -1
        ans = len(wordsDict)

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                idx_1 = i
            elif wordsDict[i] == word2:
                idx_2 = i

            if idx_1 != -1 and idx_2 != -1:
                ans = min(ans, abs(idx_1 - idx_2))

        return ans


wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = 'coding'
word2 = 'practice'
print(Solution().shortestDistance(wordsDict, word1, word2))
word1 = 'makes'
word2 = 'coding'
print(Solution().shortestDistance(wordsDict, word1, word2))


"""
- make two pointers
  - each is the most recent index
"""


from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        p1 = -1
        p2 = -1
        ans = len(wordsDict)

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                p1 = i
            elif wordsDict[i] == word2:
                p2 = i

            if p1 != -1 and p2 != -1:
                ans = min(ans, abs(p1 - p2))

        return ans


wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"
print(Solution().shortestDistance(wordsDict, word1, word2))


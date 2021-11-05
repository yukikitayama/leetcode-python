from typing import List
import collections


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word_to_indices = collections.defaultdict(list)
        for i, word in enumerate(wordsDict):
            word_to_indices[word].append(i)

        indices1 = word_to_indices[word1]
        indices2 = word_to_indices[word2]
        p1 = 0
        p2 = 0
        ans = float('inf')
        while p1 < len(indices1) and p2 < len(indices2):
            ans = min(ans, abs(indices1[p1] - indices2[p2]))

            if indices1[p1] < indices2[p2]:
                p1 += 1
            else:
                p2 += 1

        return ans


wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"
print(Solution().shortestDistance(wordsDict, word1, word2))


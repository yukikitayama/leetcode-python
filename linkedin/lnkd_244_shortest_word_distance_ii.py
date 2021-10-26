"""
- Worst case time O(max(len(l1), len(2)))
- l1 pointer needs to go to the end of l1
l1: [2, 3, 4, 5, 6]
l2: [10]
"""


from typing import List
import collections


class WordDistance:
    def __init__(self, wordsDict: List[str]):
        # Time spends O(n) to make the dictionary
        self.locations = collections.defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.locations[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        ans = float('inf')

        loc1 = self.locations[word1]
        loc2 = self.locations[word2]
        l1 = l2 = 0

        # Time spends O(max(len(loc1), len(loc2)))
        while l1 < len(loc1) and l2 < len(loc2):
            ans = min(ans, abs(loc1[l1] - loc2[l2]))

            if loc1[l1] > loc2[l2]:
                l2 += 1
            else:
                l1 += 1

        return ans


wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
obj = WordDistance(wordsDict)
print(obj.shortest('coding', 'practice'))
print(obj.shortest('makes', 'coding'))

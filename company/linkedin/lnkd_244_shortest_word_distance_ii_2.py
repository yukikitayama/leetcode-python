"""
- Constructor makes hashmap with key word and value an array of the indices in wordsDict
- All the arrays will be ascending
- Take difference
  - if word1 index is smaller, increment word1 index
  - If word3 index is smaller, increment word2 index

- a: [1, 2]
- b: [3]

- a: [3, 4]
- b: [1, 2]
"""


from typing import List
import collections


class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.word_to_indices = collections.defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.word_to_indices[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        min_distance = float('inf')
        indices1 = self.word_to_indices[word1]
        indices2 = self.word_to_indices[word2]
        p1 = 0
        p2 = 0
        while p1 < len(indices1) and p2 < len(indices2):
            num1 = indices1[p1]
            num2 = indices2[p2]
            distance = abs(num1 - num2)
            min_distance = min(distance, min_distance)
            if num1 < num2 and p1 != len(indices1) - 1:
                p1 += 1

            elif num1 < num2 and p1 == len(indices1) - 1:
                p2 += 1

            elif num1 > num2 and p2 != len(indices2) - 1:
                p2 += 1

            elif num1 > num2 and p2 == len(indices2) - 1:
                p1 += 1

        return min_distance


wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
obj = WordDistance(wordsDict)
print(obj.shortest('coding', 'practice'))
print(obj.shortest('makes', 'coding'))

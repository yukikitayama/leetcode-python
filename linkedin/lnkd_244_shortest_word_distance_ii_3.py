from typing import List
import collections


class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.word_to_indices = collections.defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.word_to_indices[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        indices1 = self.word_to_indices[word1]
        indices2 = self.word_to_indices[word2]
        p1 = 0
        p2 = 0
        ans = float('inf')
        while p1 < len(indices1) and p2 < len(indices2):
            distance = abs(indices1[p1] - indices2[p2])
            ans = min(ans, distance)

            if indices1[p1] < indices2[p2]:
                p1 += 1
            else:
                p2 += 1
        return ans


"""
Idea
- Constructor makes a hashmap with key word and value list of indices
- Shortest() gets two list from the hashmap
  - Initialize pointer to word1 and pointer to word2 to 0
  - Use two indices to calculate distance
  - if word1 pointer is smaller than word2 pointer
    - Move word1 pointer
  - Else
    - Move word2 pointer
    
Complexity
- Time
  - Let
  
Test
- makes: [1, 4]
- coding: [3]

- a: [2, 3, 4]
- b: [1]
"""


wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
obs = WordDistance(wordsDict)
print(obs.shortest('coding', 'practice'))
print(obs.shortest('makes', 'coding'))




